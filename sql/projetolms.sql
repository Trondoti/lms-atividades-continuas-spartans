create database LMS
go
use LMS
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
,DtExpiração DATE DEFAULT GETDATE()
,RA varchar (20) --inserir *Foto
, PRIMARY KEY (ID)
)

go
CREATE TABLE Professor(
ID INT
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
)
 

