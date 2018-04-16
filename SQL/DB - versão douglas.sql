create database LMS24
go
use LMS24
go
CREATE TABLE Coordenador(
ID INT 
,LOGON VARCHAR (20) UNIQUE
,Senha VARCHAR (20) not null
,Nome VARCHAR(30) not null
,Email VARCHAR  (40) UNIQUE not null
,Celular CHAR(9)  UNIQUE
, DtExpiração DATE DEFAULT GETDATE()
, PRIMARY KEY (ID)
)
go
CREATE TABLE Aluno(
ID INT
,LOGON VARCHAR (20) UNIQUE
,Senha VARCHAR (20) not null
,Nome VARCHAR(30) not null
,Email VARCHAR  (40) UNIQUE not null
,Celular CHAR(9)  UNIQUE
,foto varchar (255) null
,DtExpiração DATE DEFAULT GETDATE()
,RA varchar (20)
, PRIMARY KEY (ID)
)

go
CREATE TABLE Professor(
ID INT not null
,LOGON VARCHAR (20) UNIQUE
,Senha VARCHAR (20) not null
,Nome VARCHAR(30) not null
,Email VARCHAR  (40) UNIQUE not null
,Celular CHAR(9)  UNIQUE
,DtExpiração DATE DEFAULT GETDATE()
,Apelido VARCHAR (20)
,PRIMARY KEY (ID)
)
go
CREATE TABLE Disciplina(
ID INT
,Nome VARCHAR (30) UNIQUE
,Data DATE DEFAULT GETDATE()
,status_disc VARCHAR (20) DEFAULT('ABERTO') 
,Plano_de_ensino varchar (1000)
,CargaHoraria INT
CHECK(CargaHoraria = 80 or CargaHoraria = 40)
,Competencias VARCHAR (1000)
,Habilidades VARCHAR (1000)
,Ementa VARCHAR (1000)
,Conteudo_Programatico VARCHAR (1000)
,Bibliografia_Basica VARCHAR (1000)
,Bibliografia_Complementar VARCHAR (1000)
,Percentual_Pratico INT
CHECK(Percentual_Pratico >=0 AND Percentual_Pratico <= 100)
,Percentual_Teorico INT
CHECK(Percentual_Teorico >=0 AND Percentual_Teorico <= 100)
,IdCoordenador int not null 
,CONSTRAINT fkIdCoordenador foreign key(IdCoordenador)
references Coordenador (ID)
,constraint pkDisciplina primary key (ID)
)
 go

 go
create table Curso
(
Id int primary key not null identity(1,1)
,Nome varchar(30) unique not null
)
create table DisciplinaOfertada

(
ID int identity(1,1) PRIMARY KEY,
IdCoordenador int not null
,DtInicioMatricula date null
,DtFimMatricula date null
,IdDisciplina int not null
,IdCurso int not null
,Ano int not null
,Semestre int not null
,Turma varchar(6)
,IdProfessor int null
,Metodologia varchar(1000) null
,Recursos varchar(1000) null
,CriterioAvaliacao varchar(1000) null
,PlanoDeAulas varchar(1000) null
,CONSTRAINT FK_IdCoordenador FOREIGN KEY (IdCoordenador) REFERENCES Coordenador(ID)
,CONSTRAINT FK_IdDisciplina FOREIGN KEY (IdDisciplina) REFERENCES Disciplina(ID)
,CONSTRAINT FK_IdProfessor FOREIGN KEY (IdProfessor) REFERENCES Professor(ID)
,CONSTRAINT CK_Ano CHECK (Ano between 1900 and 2100)
,CONSTRAINT CK_Semestre CHECK (Semestre between 1 and 2)
,CONSTRAINT CK_Turma CHECK (Turma between 'A' and 'Z')
,constraint fkCurso foreign key (IdCurso)
references Curso (ID)
)

go
create table SolicitacaoMatricula
(
ID int identity (1,1) primary key
,IDAluno int not null
,IDDisciplinaOfertada int not null
,DtSolicitacao date default getdate() not null
,IDCoordenador int null
,[Status] varchar (100) default 'Solicitada' CHECK ([Status]= 'Solicitada' or [Status]= 'Aprovada' or [Status]= 'Rejeitada' or [Status]= 'Cancelada')

,CONSTRAINT FK_IDAluno FOREIGN KEY (IDAluno) REFERENCES Aluno (ID)
,CONSTRAINT FK_IDDisciplinaOfertada FOREIGN KEY (IDDisciplinaOfertada) REFERENCES DisciplinaOfertada (ID)
,CONSTRAINT FK_IDCoordenadorSC FOREIGN KEY (IDCoordenador) REFERENCES Coordenador (ID)
)
go
create table atividade
(
id int not null primary key identity (1,1)
,titulo varchar (50) unique
,descricao varchar (1000) not null
,conteudo varchar (1000) null
,tipo varchar (50) CHECK(tipo = 'Resposta aberta' or tipo = 'Teste')
,extra varchar (1000) null
,idProfessor int not null foreign key
references professor (ID)
)

go
create table Atividade_Vinculada(
ID int not null
,professor int not null
,atividade int not null
,disciplinaofertada int not null
,rotulo varchar (100) not null unique (atividade,disciplinaofertada)
,CONSTRAINT fk_Atividade FOREIGN KEY (atividade) references atividade (ID) 
,CONSTRAINT fk_professor FOREIGN KEY (professor) references Professor (ID)
,CONSTRAINT fkDisciplinaofertada FOREIGN KEY (disciplinaofertada) references DisciplinaOfertada (ID)
,Estado varchar (100)
,Dt_inicio_respostas Date
,Dt_fim_respostas Date 
,constraint pkAV primary key (ID)

)
go
create table Entrega
(
ID int identity(1,1) primary key,
idAluno int NOT NULL,
Titulo VARCHAR (40),
Resposta VARCHAR(1000),
atividadeVinculada int not null
,DtEntrega DATE DEFAULT GETDATE() NOT NULL,
[Status] VARCHAR(20) DEFAULT('ENTREGUE') CHECK([Status] = 'ENTREGUE' or [Status] = 'CORRIGIDO'),
idProfessor int NOT NULL,
Nota decimal(4,2) NOT NULL,
DtAvaliacao date NOT NULL,
Obs VARCHAR(1000),


CONSTRAINT fkAluno FOREIGN KEY (idAluno) references Aluno (ID),
CONSTRAINT fkProfessor FOREIGN KEY (idProfessor) references Professor (ID),
CONSTRAINT CK_Nota CHECK (Nota between 0 and 10)
,constraint fkAtividadeVinculada foreign key (atividadeVinculada)
references Atividade_Vinculada (ID)

)
go
create table mensagem
(
id int not null primary key identity (1,1)
,IdAluno int not null
,IdProfessor int not null
,Assunto varchar (1000) null
,Referencia varchar (1000) null
,conteudo varchar (1000) null
,[Status] varchar (50) CHECK([status] = 'Enviado' or [status] = 'Lido' or [status] = 'Respondido')
,DtEnvio date default getdate()
,DtResposta date not null
,Resposta varchar (1000) null
,constraint fkAlunoMensagem foreign key (idAluno) references aluno (ID)
,constraint fkProfessorMensagem foreign key (idProfessor) references professor (ID)
)


insert into Coordenador(ID,LOGON,Senha,Nome,Email,Celular)
Values(01,'GabrielCoordenador','impacta','Gabriel','gabrielcod@gmail.com','999999999')
---------------------------------------------------------------------------------------------
insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(01,'PabloImpacta','impacta','Pablo','pabloaluno@gmail.com','999999999','10000')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(02,'LuizImpacta','impacta','Luiz','luizaluno@gmail.com','999999987','10001')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(03,'MarcosImpacta','impacta','Marcos','marcoaluno@gmail.com','99999923','10002')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(04,'GuilhermeImpacta','impacta','Guilherme','guialuno@gmail.com','99999943','10003')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(05,'LucasImpacta','impacta','Lucas','lucasaluno@gmail.com','999999943','10004')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(06,'DouglasImpacta','impacta','Douglas','dougaluno@gmail.com','999999234','10005')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(07,'FraImpacta','impacta','Françoise','franaluno@gmail.com','999999453','10006')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(08,'Juliaimpacta','impacta','Julia','Juliaaluno@gmail.com','999995467','10007')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(09,'Jesusimpacta','impacta','Jesus','jesusaluno@gmail.com','999992314','10008')

insert into Aluno(ID,LOGON,Senha,Nome,Email,Celular,RA)
Values(10,'Milaimpacta','impacta','Mila','milaaluno@gmail.com','999362314','10009')
---------------------------------------------------------------------------------------------
insert into Curso(Nome)
Values('ADS')

insert into Curso(Nome)
Values('ADM')

insert into Curso(Nome)
Values('BD')

insert into Curso(Nome)
Values('GTI')

insert into Curso(Nome)
Values('JD')

insert into Curso(Nome)
Values('PG')

insert into Curso(Nome)
Values('PM')

insert into Curso(Nome)
Values('REDES')

insert into Curso(Nome)
Values('SI')
-----------------------------------------------------------------------------------
insert into Disciplina(ID,Nome,Plano_de_ensino,CargaHoraria,Competencias,Habilidades,Ementa,Conteudo_Programatico,Bibliografia_Basica,Bibliografia_Complementar,Percentual_Pratico,Percentual_Teorico,IdCoordenador)
Values(01,'Linguagem SQL','Conceitos basicos, Linguagem SQL, Manipulação de Dados e etc..' ,80,'Arquitetar um Banco de dados, Garantir a integridade e criar relatorios','Conhecimento aprofundado sobre SQL e sua linguagem',
'Introdução a linguagem,Linguagem de Manipulação de dados, Funções e Visões','Historia da Linguagem, O modelo fisico, Create, Alter, Drop e Update, Insert, Delete e Join,Revisao e Prova ','DATE, C.J. SQL e Teoria Relacional: Como escrever codigos em SQL precisos - São Paulo:Novatec, 2015','ELMASRI, R.E.; NAVATHE, S. B. Sistemas de Banco de Dados. Ed. São Paulo: Pearson. 2011',75,25,01)

insert into Disciplina(ID,Nome,status_disc,Plano_de_ensino,CargaHoraria,Competencias,Habilidades,Ementa,Conteudo_Programatico,Bibliografia_Basica,Bibliografia_Complementar,Percentual_Pratico,Percentual_Teorico,IdCoordenador)
Values(02,'Tecnologia Web','ABERTO','Conceitos basicos de HTML5,CSS3,JavaScripts ao avançado, Introdução e ferramentas ao Django',80,'Desenvolver aplicação Web','Conhecer e dominar as principais maneiras de  construção de publicação de um site utilizando HTML5, CSS3 e JavaScripts',
'Tecnologias para desenvolvimento de aplicações web com HTML5,CSS3 e JavaScripts','Introdução a HTML5,CSS3 e JavaScripts programação avançada, revisão e prova','Use a Cabeça!, HTML5 com CSS3.Rio de Janeiro: Alta Books, 2 edição, 2015','Moraes, Construindo Aplicações Web. São Paulo, NovaTec,2015',50,50,01)

------------------------------------------------------------------------------------------------------------------------
insert into Professor(ID,LOGON,Senha,Nome,Email,Celular)
values(01,'Erick_prof','impacta','Erick','erickimpacta@gmail.com',999998886)

----------------------------------------------------------------------------------------------------------------------------
insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (05,01,'2018-04-03',01)

insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (04,01,'2018-04-08',01)

insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (03,01,'2018-03-05',01)

insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (02,02,'2018-06-03',01)


insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (01,02,'2018-06-12',01)


insert into SolicitacaoMatricula (IDAluno,IDDisciplinaOfertada,DtSolicitacao, IDCoordenador)
values (07,02,'2018-05-22',01)
-------------------------------------------------------------------------------------------------------------------------------------



insert into DisciplinaOfertada(IdCoordenador,DtInicioMatricula,DtFimMatricula,IdDisciplina,IdCurso,Ano,Semestre,Turma,IdProfessor,Metodologia,Recursos,CriterioAvaliacao,PlanoDeAulas)
values(01,'2018-04-16','2019-04-16',01,01,2018,01,'ADS2B',01,'Aulas utilizando projetor, lousa e computador, cada aula terá 50 minutos e atividades contínuas diárias.',
'Maquiná virtual com servidor Microsoft SQL Server 2014','Nota Final = 60% MAC + 40% Prova e Frequência 75% ','Historia da Linguagem, O modelo fisico, Create, Alter, Drop e Update, Insert, Delete e Join,Revisao e Prova ')

insert into DisciplinaOfertada(IdCoordenador,DtInicioMatricula,DtFimMatricula,IdDisciplina,IdCurso,Ano,Semestre,Turma,IdProfessor,Metodologia,Recursos,CriterioAvaliacao,PlanoDeAulas)
values(01,'2018-02-10','2024-04-02',02,09,2018,02,'SI2B',01,'Aulas utilizando projetor, lousa e computador, cada aula terá 50 minutos e atividades contínuas diárias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequência 75% ','Tecnologias para desenvolvimento de aplicações web com HTML5,CSS3 e JavaScripts')

-------------------------------------------------------------------------------------------------------------------------------------------------------------

update SolicitacaoMatricula set [Status] = 'Aprovada' where ID = 02

update SolicitacaoMatricula set [Status] = 'Rejeitada' where ID = 03

update SolicitacaoMatricula set [Status] = 'Cancelada' where ID = 06
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

insert into atividade (titulo,descricao,conteudo,idProfessor)
values('Construção de formulários com HTML5','Construir um formulário que tenha campos login e senha','Verificar os slides da aula anterior',01)

insert into atividade (titulo,descricao,conteudo,idProfessor)
values('Layout do formulário','Construir o CSS3 do formulário de Login','Verificar os slides da aula anterior',01)



select *
from atividade

delete from SolicitacaoMatricula

sp_help atividade

