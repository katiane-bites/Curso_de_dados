create table turma (sigla varchar(10) not null,ano_sem varchar(6));
create table sala (capacidade varchar odigo varchar(10) not null unique);
create table predio (codigo varchar(128) not null);
create table disciplina(codigo varchar(70) not null);
create table curruculo (obrig_opc(64));
create table curso (codigo varchar(10) not null);
Alter table curso add column id serial pk_curso primary key (id);
Alter table disciplina add column id nstraint pk_disciplina primary key (id);
Alter table predio add column id seriaint pk_predio primary key (id);
Alter table turma add column id seriaint pk_turma primary key (id);
Alter table sala add column id_predio integer not null,add constraint fk_sala_predio foreign key (id_predio) references predio (id);
Alter table turma add column sala_id int references sala(id);
Alter table turma add column disciplina_id int references disciplina(id);
Alter table curriculo add column disciplina_id int references disciplina(id), add column curso_id int references curso(id);



