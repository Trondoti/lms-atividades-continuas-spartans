create database LMS24
go
use LMS24
go
CREATE TABLE Coordenador(
ID int identity(1,1) 
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
ID int identity(1,1) 
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
ID int identity(1,1) 
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
ID int identity(1,1)
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
Id int identity(1,1) primary key 
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
id int primary key identity (1,1)
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
ID int int identity(1,1) 
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
id int identity (1,1) primary key 
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


