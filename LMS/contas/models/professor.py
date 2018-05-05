from django.db import models
from .pessoa import Pessoa

class Professor(Pessoa):
    idprofessor = models.AutoField(db_column='idProfessor', primary_key=True)  # Field name made lowercase.
    apelido = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'

    def __str__(self):
        return self.nome