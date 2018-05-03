from django.db import models

class Aluno(models.Model):
    idaluno = models.AutoField(db_column='idAluno', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=11, blank=True, null=True)
    foto = models.CharField(max_length=11, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    ra = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aluno'

    def __str__(self):
        return self.nome

class Coordenador(models.Model):
    idcoordenador = models.AutoField(db_column='idCoordenador', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'coordenador'

    def __str__(self):
        return self.nome

class Professor(models.Model):
    idprofessor = models.AutoField(db_column='idProfessor', primary_key=True)  # Field name made lowercase.
    logon = models.CharField(unique=True, max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.CharField(unique=True, max_length=40)
    celular = models.CharField(unique=True, max_length=9, blank=True, null=True)
    dtexpiracao = models.DateField(db_column='dtExpiracao', blank=True, null=True)  # Field name made lowercase.
    apelido = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professor'

    def __str__(self):
        return self.nome

class Mensagem(models.Model):
    idmensagem = models.AutoField(db_column='idMensagem', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='idAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='idProfessor')  # Field name made lowercase.
    assunto = models.CharField(max_length=1000, blank=True, null=True)
    referencia = models.CharField(max_length=1000, blank=True, null=True)
    conteudo = models.CharField(max_length=1000, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    dtenvio = models.DateField(db_column='dtEnvio', blank=True, null=True)  # Field name made lowercase.
    dtresposta = models.DateField(db_column='dtResposta')  # Field name made lowercase.
    resposta = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mensagem'

    def __str__(self):
        pass
