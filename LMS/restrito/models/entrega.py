from django.db import models
from contas.models.aluno import Aluno
from contas.models.professor import Professor
from curriculo.models import Disciplina,Disciplinaofertada, Curso



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
