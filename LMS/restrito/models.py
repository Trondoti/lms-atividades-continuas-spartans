from django.db import models
from contas.models import Aluno,Coordenador,Professor
from curriculo.models import Disciplina,Disciplinaofertada, Curso



class Solicitacaomatricula(models.Model):
    idsolicitacaomatricula = models.AutoField(db_column='idSolicitacaoMatricula', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada')  # Field name made lowercase.
    dtsolicitacao = models.DateField(db_column='dtSolicitacao')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='idCoordenador', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitacaoMatricula'

class Atividade(models.Model):
    idatividade = models.AutoField(db_column='idAtividade', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=1000)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    extra = models.CharField(max_length=1000, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividade'

    def __str__(self):
        return self.titulo

class Atividadevinculada(models.Model):
    idatividadevinculada = models.AutoField(db_column='idAtividadeVinculada', primary_key=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='idAtividade')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='idDisciplinaOfertada')  # Field name made lowercase.
    rotulo = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, blank=True, null=True)
    dtiniciorespostas = models.DateField(db_column='dtInicioRespostas', blank=True, null=True)  # Field name made lowercase.
    dtfimrespostas = models.DateField(db_column='dtFimRespostas', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'atividadeVinculada'
        unique_together = (('idatividade', 'iddisciplinaofertada'),)


    def __str__(self):
        return self.rotulo


class Entrega(models.Model):
    identrega = models.AutoField(db_column='idEntrega', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    titulo = models.CharField(max_length=40, blank=True, null=True)
    resposta = models.CharField(max_length=1000, blank=True, null=True)
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='idAtividadeVinculada')  # Field name made lowercase.
    dtentrega = models.DateField(db_column='dtEntrega')  # Field name made lowercase.
    status = models.CharField(max_length=20, blank=True, null=True)
    idprofessor = models.ForeignKey(Professor, models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    nota = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    dtavaliacao = models.DateField(db_column='dtAvaliacao')  # Field name made lowercase.
    obs = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entrega'
    
    def __str__(self):
        return self.titulo
