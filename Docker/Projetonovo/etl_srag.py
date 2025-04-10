import pandas as pd
from sqlalchemy import create_engine

# Conexão com PostgreSQL (ajuste as crendencias conforme necessario)
engine = create_engine("postgresql://admin:admin@postgres:5432/datawarehouse")

# Carregamento dados públicos
df = pd.read_csv("srag_2021.csv", sep=";", encoding="utf-8", low_memory=False)

#Filtro colunas relevantes e removendo nulos
df = df[["DT_NOTIFIC", "CS_SEXO", "NU_IDADE_N","CLASSI_FIN","EVOLUCAO", "SG_UF_NOT"]].dropna()

#Criando dimensão de faixa etária
def faixa_etaria(idade):
    if idade < 10:
        return "0-9"
    elif idade <20:
        return "10-19"
    elif idade < 40:
        return "20-39"
    elif idade < 60:
        return "40-59"
    else:
        return "60+"
    
df["faixa_etaria"] = df["NU_IDADE_N"].apply(faixa_etaria)


#Criando tabelas dimencionais com IDs
dim_regiao = df[["SG_UF_NOT"]].drop_duplicates().reset_index(drop=True)
dim_regiao["id_regiao"] = dim_regiao.index + 1
dim_regiao.rename(columns={"SG_UF_NOT": "nome_regiao"}, inplace=True)
dim_regiao.to_sql("dim_regiao", engine, if_exists="replace", index=False)

df = df.merge(dim_regiao, left_on="SG_UF_NOT", right_on="nome_regiao")

print("ETL carregado com sucesso!!")

