from django.db import models
from django.utils import timezone

# Create your models here.
'''class noticias(models.Model):
    name = model.CharField('Nome', max_length = 100)
    image = models.ImageField(upload_to 'img/noticias'), verbose_name = 'Imagem',
    null = True, blank = True'''


class coordenador(models.Model):#ok
    logon = models.CharField(unique=True, max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=40)
    celular = models.IntegerField(unique=True, null=True)
    dtExpiracao = models.DateField(default=timezone.now) 

class aluno(models.Model):#ok
    logon = models.CharField(unique=True, max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=40)
    celular = models.IntegerField(unique=True, null=True)
    foto = models.CharField(null=True, max_length=255)   
    dtExpiracao = models.DateField(default=timezone.now) 
    ra = models.CharField(unique=True,max_length=20)

class professor(models.Model):#ok
    logon = models.CharField(unique=True, max_length=20)
    senha = models.CharField(max_length=20)
    nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True, max_length=40)
    celular = models.IntegerField(unique=True, null=True)
    dtExpiracao = models.DateField(default=timezone.now) 
    apelido = models.CharField(null=True, max_length=20)

class disciplina(models.Model):#Ok
    checkCarg =  (
        (80,"80 horas"),
        (40, "40 horas"),
    )
    checkStatus = (
        ('Aberta','Aberta'),
        ('Fechada','Fechada'),
    )
    nome = models.CharField(unique=True, max_length=30)
    data = models.DateField(null=True, default=timezone.now)
    statusDisc = models.CharField(choices=checkStatus,null=True, default='Aberto', max_length=20)
    planoDeEnsino = models.TextField()
    cargaHoraria = models.IntegerField(choices=checkCarg)
    competencias = models.TextField()
    habilidades = models.TextField()
    ementa = models.TextField()
    conteudoProgramatico = models.TextField()
    bibliografiaBasica = models.TextField()
    bibliografiaComplementar = models.TextField()
    percentualPratico = models.IntegerField()#Precisa do check
    percentualTeorico = models.IntegerField()#Precisa do check
    idCoordenador = models.ForeignKey(coordenador,on_delete=models.CASCADE) 
    
class mensagem(models.Model):#Ok
    checkStatus = (
        ('Enviado', 'Enviado'),
        ('Lido', 'Lido'),
        ('Respondido', 'Respondido'),
    )
    idAluno = models.ForeignKey(aluno, on_delete=models.CASCADE)
    idProfessor = models.ForeignKey(professor, on_delete = models.CASCADE)
    assunto = models.TextField()
    referencia = models.TextField(blank=True, null=True)
    conteudo = models.TextField()
    status = models.CharField(choices=checkStatus, max_length=10,default='Enviado')
    dtEnvio = models.DateField(default=timezone.now)
    dtResposta = models.DateField(blank=True, null=True,default= timezone.now)
    resposta = models.TextField(blank=True, null=True)
    
class curso(models.Model):#Ok
    nome = models.CharField(max_length=30, unique=True)

class atividade(models.Model):#Ok
    checkTipo = (
        ('Aberta','Aberta'),
        ('Teste','Teste'),
    )
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    conteudo = models.TextField(null=True, blank=True)
    tipo = models.CharField(choices=checkTipo,max_length=6)
    extra = models.TextField(null=True, blank=True)
    idProfessor = models.ForeignKey(professor, on_delete=models.CASCADE)

class atividadeVinculada(models.Model):#ok
    professor = models.ForeignKey(professor, on_delete=models.CASCADE)
    atividade = models.ForeignKey(atividade,on_delete=models.CASCADE)
    #disciplinaOfertada = models.ForeignKey(disciplinaOfertada,on_delete=models.CASCADE)
    rotulo = models.CharField(max_length=100,unique=True)
    estado = models.CharField(max_length=100)
    dtInicioRespostas = models.DateField(null=True,blank=True)
    dtFimRespostas = models.DateField(null=True,blank=True)

class entrega (models.Model):#ok
    checkStatus = (
        ('Entregue','Entregue'),
        ('Corrigido','Corrigido')
    )
    idAluno = models.ForeignKey(aluno,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=40)
    resposta = models.TextField()
    atividadeVinculada = models.ForeignKey(atividadeVinculada, on_delete=models.CASCADE)
    dtEntrega = models.DateField(default=timezone.now)
    status = models.CharField(null=True,max_length=10,default='Entregue',choices=checkStatus) 
    idProfessor = models.ForeignKey(professor,on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=2,decimal_places=2) 
    dtAvaliacao = models.DateField()  
    obs = models.TextField(null=True,blank=True)


