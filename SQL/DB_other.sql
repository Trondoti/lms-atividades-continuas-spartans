
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
Values(07,'FraImpacta','impacta','Francoise','franaluno@gmail.com','999999453','10006')

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
'Máquina virtual com servidor Microsoft SQL Server 2014','Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Historia da Linguagem, O modelo fisico, Create, Alter, Drop e Update, Insert, Delete e Join,Revisao e Prova ')

insert into DisciplinaOfertada(IdCoordenador,DtInicioMatricula,DtFimMatricula,IdDisciplina,IdCurso,Ano,Semestre,Turma,IdProfessor,Metodologia,Recursos,CriterioAvaliacao,PlanoDeAulas)
values(01,'2018-02-10','2024-04-02',02,09,2018,02,'SI2B',01,'Aulas utilizando projetor, lousa e computador, cada aula terá 50 minutos e atividades contínuas diárias.','Computadores com softwares apropriados para a disciplina',
'Nota Final = 60% MAC + 40% Prova e Frequencia 75% ','Tecnologias para desenvolvimento de aplicações web com HTML5,CSS3 e JavaScripts')

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
