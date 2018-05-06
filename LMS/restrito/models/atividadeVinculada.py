from django.db import models
from contas.models.aluno import Aluno
from contas.models.professor import Professor
from contas.models.coordenador import Coordenador
from curriculo.models import Disciplina,Disciplinaofertada, Curso


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