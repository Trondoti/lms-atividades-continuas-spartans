CREATE DATABASE LMS24

GO
USE LMS24

GO
CREATE TABLE coordenador (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR (30) NOT NULL
, email VARCHAR (40) UNIQUE not null
, celular CHAR (9) UNIQUE
, dtExpiracao DATE DEFAULT GETDATE()
)

GO
CREATE TABLE aluno (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR (30) NOT NULL
, email VARCHAR (40) UNIQUE NOT NULL
, celular CHAR (9) UNIQUE
, foto VARCHAR (255) NULL
, dtExpiracao DATE DEFAULT GETDATE()
, ra VARCHAR (20)
, desconto INT NOT NULL DEFAULT 0
)

GO
CREATE TABLE professor (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, logon VARCHAR (20) UNIQUE
, senha VARCHAR (20) NOT NULL
, nome VARCHAR (30) NOT NULL
, email VARCHAR (40) UNIQUE NOT NULL
, celular CHAR (9) UNIQUE
, dtExpiracao DATE DEFAULT GETDATE()
, apelido VARCHAR (20)
)

GO
CREATE TABLE disciplina (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, nome VARCHAR (30) UNIQUE
, data DATE DEFAULT GETDATE()
, statusDisc VARCHAR (20) DEFAULT('ABERTO')
, planoDeEnsino VARCHAR (1000)
, cargaHoraria INT CHECK(cargaHoraria = 80 OR cargaHoraria = 40)
, competencias VARCHAR (1000)
, habilidades VARCHAR (1000)
, ementa VARCHAR (1000)
, conteudoProgramatico VARCHAR (1000)
, bibliografiaBasica VARCHAR (1000)
, bibliografiaComplementar VARCHAR (1000)
, mensalidade DECIMAL (6,2) NOT NULL
, percentualPratico INT CHECK(percentualPratico >= 0 AND percentualPratico <= 100)
, percentualTeorico INT CHECK(percentualTeorico >= 0 AND percentualTeorico <= 100)
, idCoordenador INT NOT NULL
, CONSTRAINT disciplina_fkIdCoordenador FOREIGN KEY(idCoordenador) REFERENCES coordenador(id)
)

GO
CREATE TABLE curso (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, nome VARCHAR (30) UNIQUE NOT NULL
)

GO
CREATE TABLE disciplinaOfertada (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, idCoordenador INT NOT NULL
, dtInicioMatricula DATE NULL
, dtFimMatricula DATE NULL
, IdDisciplina INT NOT NULL
, idCurso INT NOT NULL
, ano INT NOT NULL
, semestre INT NOT NULL
, turma VARCHAR (6)
, idProfessor INT NULL
, metodologia VARCHAR (1000) NULL
, recursos VARCHAR (1000) NULL
, criterioAvaliacao VARCHAR (1000) NULL
, planoDeAulas VARCHAR (1000) NULL
, CONSTRAINT disciplinaOfertada_fKIdCoordenador FOREIGN KEY (idCoordenador) REFERENCES coordenador(id)
, CONSTRAINT disciplinaOfertada_fkIdDisciplina FOREIGN KEY (idDisciplina) REFERENCES disciplina(id)
, CONSTRAINT disciplinaOfertada_fkIdProfessor FOREIGN KEY (idProfessor) REFERENCES professor(id)
, CONSTRAINT disciplinaOfertada_ckAno CHECK (ano BETWEEN 1900 AND 2100)
, CONSTRAINT disciplinaOfertada_ckSemestre CHECK (semestre BETWEEN 1 AND 2)
, CONSTRAINT disciplinaOfertada_ckTurma CHECK (turma BETWEEN 'A' AND 'Z')
, CONSTRAINT disciplinaOfertada_fkCurso FOREIGN KEY (idCurso) REFERENCES curso (id)
)

GO
CREATE TABLE solicitacaoMatricula (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, idAluno INT NOT NULL
, idDisciplinaOfertada INT NOT NULL
, dtSolicitacao DATE DEFAULT GETDATE() NOT NULL
, idCoordenador INT NULL
, [status] VARCHAR (100) DEFAULT 'SOLICITADA' CHECK ([status]= 'SOLICITADA' or [status]= 'APROVADA' or [status]= 'REJEITADA' or [status]= 'CANCELADA')
, CONSTRAINT solicitacaoMatricula_fkIdAluno FOREIGN KEY (idAluno) REFERENCES aluno(id)
, CONSTRAINT solicitacaoMatricula_fkIdDisciplinaOfertada FOREIGN KEY (idDisciplinaOfertada) REFERENCES disciplinaOfertada(id)
, CONSTRAINT solicitacaoMatricula_fkIdCoordenador FOREIGN KEY (idCoordenador) REFERENCES coordenador(id)
)

GO
CREATE TABLE atividade (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, idProfessor INT NOT NULL
, titulo VARCHAR (50)
, descricao VARCHAR (1000) NOT NULL
, conteudo VARCHAR (1000) NULL
, tipo VARCHAR (50) CHECK(tipo = 'RESPOSTA ABERTA' or tipo = 'TESTE')
, extra VARCHAR (1000) NULL
, CONSTRAINT atividade_fkIdCoordenador FOREIGN KEY (idProfessor) REFERENCES professor(id)
)

GO
CREATE TABLE atividadeVinculada (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, professor INT NOT NULL
, atividade INT NOT NULL
, disciplinaOfertada INT NOT NULL
, rotulo VARCHAR (100) NOT NULL UNIQUE (atividade, disciplinaOfertada)
, estado VARCHAR (100)
, dtInicioRespostas DATE
, dtFimRespostas DATE
, CONSTRAINT atividadeVinculada_fkAtividade FOREIGN KEY (atividade) REFERENCES atividade(id)
, CONSTRAINT atividadeVinculada_fkProfessor FOREIGN KEY (professor) REFERENCES professor(id)
, CONSTRAINT atividadeVinculada_fkDisciplinaOfertada FOREIGN KEY (disciplinaOfertada) REFERENCES disciplinaOfertada(id)
)

GO
CREATE TABLE entrega (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, idAluno INT NOT NULL
, titulo VARCHAR (40)
, resposta VARCHAR (1000)
, atividadeVinculada INT NOT NULL
, dtEntrega DATE DEFAULT GETDATE() NOT NULL
, [status] VARCHAR (20) DEFAULT('ENTREGUE') CHECK([status] = 'ENTREGUE' or [status] = 'CORRIGIDO')
, idProfessor INT NOT NULL
, nota DECIMAL (4,2) NOT NULL
, dtAvaliacao DATE NOT NULL
, obs VARCHAR (1000)
, CONSTRAINT entrega_fkAluno FOREIGN KEY (idAluno) REFERENCES aluno(id)
, CONSTRAINT entrega_fkProfessor FOREIGN KEY (idProfessor) REFERENCES professor(id)
, CONSTRAINT entrega_ckNota CHECK (nota BETWEEN 0 AND 10)
, CONSTRAINT entrega_fkAtividadeVinculada FOREIGN KEY (atividadeVinculada) REFERENCES atividadeVinculada(id)
)

GO
CREATE TABLE mensagem (
id INT NOT NULL IDENTITY(1,1) PRIMARY KEY
, idAluno INT NOT NULL
, idProfessor INT NOT NULL
, assunto VARCHAR (1000) NULL
, referencia VARCHAR (1000) NULL
, conteudo VARCHAR (1000) NULL
, [status] VARCHAR (50) CHECK([status] = 'ENVIADO' or [status] = 'LIDO' or [status] = 'RESPONDIDO')
, dtEnvio DATE DEFAULT GETDATE()
, dtResposta DATE NOT NULL
, resposta VARCHAR (1000) NULL
, CONSTRAINT mensagem_fkAlunoMensagem FOREIGN KEY (idAluno) REFERENCES aluno(id)
, CONSTRAINT mensagem_fkProfessorMensagem FOREIGN KEY (idProfessor) REFERENCES professor(id)
)
