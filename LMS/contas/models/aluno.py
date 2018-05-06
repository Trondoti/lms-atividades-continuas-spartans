from .pessoa import Pessoa
from django.db import models

class Aluno(Pessoa):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    foto = models.CharField(max_length=11, blank=True, null=True)
    ra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'
    
    
    def __str__(self):

        return self.nome
  
   
