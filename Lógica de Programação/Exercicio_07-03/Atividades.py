#Arredondamento Valores
print("Atividade 1 \n")
preco_total = float(189.987654)
print(round(preco_total, 1))
print(round(preco_total, 2))
print(round(preco_total, 3))
print()


#Média de Notas
print("Atividade 2 \n")
nota1 = 7.356
nota2 = 8.479
nota3 = 6.825
media = (nota1 + nota2 + nota3) / 3
print("Média de notas:", round(media))
print()


#Contato Elementos
print("Atividade 3 \n")

#Lista
numeros = [5, 10, 20, 30, 35]
print(len(numeros))

#Dicionarios
dados = {"nome": "Ana", "idade": 22, "curso": "Engenharia"}
print(len(dados))

#Tupla
valores = (3.14, 2.71, 1.41)
print(len(valores))
print()


#Criando a string
print("Atividade 4 \n")
texto = "Programação em Python é divertida!"

#Fatiamentos
print(f"Primeiro caractere:", {texto[0]})
print(f"Quinto caractere:", {texto[4]})
print(f"Último caractere:", {texto[-1]})
print(f"Últimos 5 caracteres:", {texto[-5:]})
print(f"Primeiros 8 caracteres:", {texto[:8]})


#Criando a string com uma frase
print("Atividade 5 \n")

frase = "A empresa TechSoft é lider no mercado de tecnologia."

#Substituindo uma palavra na frase
frase_modificada = frase.replace("TechSoft", "InovaTech")

#Exibindo o resultado
print(frase_modificada)


#Crianco a string com uma frase
print("Atividade 6 \n")

frase = "Python é uma linguagem de programação poderosa."

#Utilizando splint() para separar as palavras
palavras = frase.split

#Exibindo o resultado
print(palavras)


#Solicitando informações ao usuário
print("Atividade 7 \n")

nome = input("Qual é o seu nome?")
cidade = input("Em qual cidade você mora?")

#Exibindo os dados digitados
print(f"Olá {nome}! Você mora em {cidade}).")


