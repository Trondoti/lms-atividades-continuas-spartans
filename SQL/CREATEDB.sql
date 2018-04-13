create database LMS20
go
use LMS20
go
CREATE TABLE Coordenador(
ID INT 
,LOGON VARCHAR (20) UNIQUE
,Senha VARCHAR (20) not null
,Nome VARCHAR(30) not null
,Email VARCHAR  (20) UNIQUE not null
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
,Email VARCHAR  (20) UNIQUE not null
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
,Email VARCHAR  (20) UNIQUE not null
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
,status_disc VARCHAR (20) DEFAULT('ABERTO') UNIQUE 
,Plano_de_ensino varchar
,CargaHoraria INT
CHECK(CargaHoraria = 80 or CargaHoraria = 40)
,Competencias VARCHAR
,Habilidades VARCHAR 
,Ementa VARCHAR 
,Conteudo_Programatico VARCHAR
,Bibliografia_Basica VARCHAR
,Bibliografia_Complementar VARCHAR
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
,Nome varchar(20) unique not null
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
,Turma varchar(1)
,IdProfessor int null
,Metodologia varchar(100) null
,Recursos varchar(100) null
,CriterioAvaliacao varchar(100) null
,PlanoDeAulas varchar(100) null
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
,descricao varchar (200) not null
,conteudo varchar (300) null
,tipo varchar (50) CHECK(tipo = 'Resposta aberta' or tipo = 'Teste')
,extra varchar (200) null
,idProfessor int not null foreign key
references professor (ID)
)

go
create table Atividade_Vinculada(
ID int not null
,professor int not null
,atividade int not null
,disciplinaofertada int not null
,rotulo varchar not null unique (atividade,disciplinaofertada)
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
Resposta VARCHAR(100),
atividadeVinculada int not null
,DtEntrega DATE DEFAULT GETDATE() NOT NULL,
[Status] VARCHAR(20) DEFAULT('ENTREGUE') CHECK([Status] = 'ENTREGUE' or [Status] = 'CORRIGIDO'),
idProfessor int NOT NULL,
Nota decimal(4,2) NOT NULL,
DtAvaliacao date NOT NULL,
Obs VARCHAR(100),


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
,Assunto varchar (300) null
,Referencia varchar (200) null
,conteudo varchar (300) null
,[Status] varchar (50) CHECK([status] = 'Enviado' or [status] = 'Lido' or [status] = 'Respondido')
,DtEnvio date default getdate()
,DtResposta date not null
,Resposta varchar (300) null
,constraint fkAlunoMensagem foreign key (idAluno) references aluno (ID)
,constraint fkProfessorMensagem foreign key (idProfessor) references professor (ID)
)

