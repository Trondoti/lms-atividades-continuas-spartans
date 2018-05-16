from django.shortcuts import render, redirect
from .models.professor import Professor
from .models.aluno import Aluno
from .models.coordenador import Coordenador
from .models.mensagem import Mensagem
from restrito.models.solicitacaoMatricula import Solicitacaomatricula
from django.db.models import Max
import base64
import hashlib
import time


def listarProfessores(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaProfessores.html', {'professores': Professor.objects.all()})

def inserirProfessor(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        email=request.POST.get("email")
        logon=request.POST.get("logon")
        try:
            professor = Professor.objects.get(email=email)
            context = {
                "mensagem": "Email já cadastrado em Professores",
                "statusCode": "500",
                "cor": "red"
            }
            return render(request, "formNovoProfessor.html", context)
        except:
            try:
                professor = Professor.objects.get(logon=logon)
                context = {
                    "mensagem": "Logon já cadastrado em Professores",
                    "statusCode": "500",
                    "cor": "red"
                }
                return render(request, "formNovoProfessor.html", context)
            except:
                try:
                    professor=Aluno.objects.get(logon=logon)
                    context = {
                        "mensagem" : "Logon já cadastrado em Alunos",
                        "statusCode": "500",
                        "cor": "red"
                    }
                    return render(request, "formNovoProfessor.html", context)
                except:
                    Professor.objects.create (
                        logon = request.POST.get('logon'),
                        senha = request.POST.get('senha'),
                        nome = request.POST.get('nome'),
                        email = request.POST.get('email'),
                        celular = request.POST.get('celular'),
                        dtexpiracao = request.POST.get('dtexpiracao'),
                        apelido = request.POST.get('apelido')
                    )
                    return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html')

def alterarProfessor(request, idprofessor):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    professor = Professor.objects.get(idprofessor=idprofessor)
    if request.method == 'POST':
       professores = Professor.objects.get(idprofessor=idprofessor)
       professores.logon = request.POST.get('logon'),
       professores.senha = request.POST.get('senha'),
       professores.nome = request.POST.get('nome'),
       professores.email = request.POST.get('email'),
       professores.celular = request.POST.get('celular'),
       professores.dtExpiracao = request.POST.get('dtexpiracao'),
       professores.apelido = request.POST.get('apelido')
       professores.save()
       return redirect('listarprofessores')
    else:
        return render(request, 'formNovoProfessor.html', {'professor': professor})


def deletarProfessor(request, idprofessor):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    professores = Professor.objects.get(idprofessor=idprofessor)
    professores.delete()
    return redirect ('listarprofessores')


def listarAlunos(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaAlunos.html', {'alunos': Aluno.objects.all()})

def inserirAluno(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        ultimoRA = Aluno.objects.all().aggregate(Max('ra'))
        file = request.FILES['foto']
        encoded = base64.b64encode(file.read())
        email=request.POST.get("email")
        logon=request.POST.get("logon")
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()
        #print(senha);
        try:
            aluno = Aluno.objects.get(email=email)
            context = {
                "mensagem" : "Email já cadastrado em alunos",
                "statusCode": "500",
                "cor": "red"
            }
            return render(request, "formNovoAluno.html", context)
        except:
            try:
                aluno=Aluno.objects.get(logon=logon)
                context = {
                    "mensagem" : "Logon já cadastrado em alunos",
                    "statusCode": "500",
                    "cor": "red"
                }
                return render(request, "formNovoAluno.html", context)
            except:
                try:
                    professor=Professor.objects.get(logon=logon)
                    context = {
                        "mensagem": "Logon já cadastrado em alunos",
                        "statusCode": "500",
                        "cor": "red"
                    }
                    return render(request, "formNovoAluno.html", context)
                except:
                    novoRA = Aluno.geraNumeroRA(ultimoRA)
                    Aluno.objects.create(
                        logon=request.POST.get("logon"),
                        senha=request.POST.get("senha"),
                        nome=request.POST.get("nome"),
                        email=request.POST.get("email"),
                        celular=request.POST.get("celular"),
                        foto=encoded,
                        ra = novoRA
                    )
                    return redirect('listaralunos')
    else:
        return render(request, "formNovoAluno.html")

def alterarAluno(request, idaluno):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.foto = aluno.foto[2:-1]
    if request.method == 'POST':
        file = request.FILES['foto']
        encoded = base64.b64encode(file.read())
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()

        aluno = Aluno.objects.get(idaluno=idaluno)
        aluno.logon=request.POST.get("logon")
        aluno.senha=request.POST.get("senha")
        aluno.nome=request.POST.get("nome")
        aluno.email=request.POST.get("email")
        aluno.celular=request.POST.get("celular")
        aluno.foto=encoded
        aluno.save()
        return redirect('listaralunos')
    else:
        return render(request, "formNovoAluno.html",  {"aluno":aluno})

def deletarAluno(request, idaluno):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.delete()
    return redirect ('listaralunos')

def listarCoordenadores(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaCoordenadores.html', {'coordenadores': Coordenador.objects.all()})

def inserirCoordenador(request):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        Coordenador.objects.create (
            logon=request.POST.get("logon"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular")
        )
        return redirect('listarcoordenadores')
    else:
        return render(request, "formNovoCoordenador.html")

def alterarCoordenador(request, idcoordenador):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    if request.method == 'POST':
        coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
        coordenador.logon=request.POST.get("logon")
        coordenador.senha=request.POST.get("senha")
        coordenador.nome=request.POST.get("nome")
        coordenador.email=request.POST.get("email")
        coordenador.celular=request.POST.get("celular")
        coordenador.save()
        return redirect('listarcoordenadores')
    else:
        return render(request, "formNovoCoordenador.html", {"coordenador": coordenador})

def deletarCoordenador(request, idcoordenador):
    try:
        if request.sessao.usuario.profile != "S":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
        
    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    coordenador.delete()
    return redirect ('listarcoordenadores')
   
   ##inicio crud mensagem 

def listarEntregas(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasAlunos.html', {"entregas": Mensagem.objects.filter(idaluno=request.sessao.usuario.id)})

def listarMensagensAlunos(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaMensagensAluno.html', {"mensagens": Mensagem.objects.filter(idaluno=request.sessao.usuario.id)})    

def listarMensagensProfessores(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaMensagensProfessor.html', {"mensagens": Mensagem.objects.filter(idprofessor=request.sessao.usuario.id)})  

def inserirMensagem(request):
    try:
        if request.sessao.usuario.profile != "A" and request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    context = {"professores" : Professor.objects.all()}
    if request.method == 'POST':
        if request.sessao.usuario.profile == 'A':
            usuario = Aluno.objects.get(idaluno=request.sessao.usuario.id)
            professor = Professor.objects.get(idprofessor=request.POST.get("professor"))
            status = 'ENVIADO'
            Mensagem.objects.create(
                idaluno=usuario,
                idprofessor=professor,
                assunto=request.POST.get("assunto"),
                referencia=request.POST.get("referencia"),
                conteudo=request.POST.get("conteudo"),
                status = status,
                resposta='',
                dtenvio=time.strftime("%Y-%m-%d"),
            )
            return redirect('listarmensagensalunos')
        else:
            status = 'RECEBIDO'
            Mensagem.objects.create(
                status = status,
                dtresposta=time.strftime("%Y-%m-%d"),
                resposta=request.POST.get("resposta"),
            )
            return redirect('listarmensagensprofessores')
    return render(request, "formNovaMensagem.html", context)

def alterarMensagem(request, idmensagem):
    try:
        if request.sessao.usuario.profile != "A" and request.sessao.usuario.profile != 'P':
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
    context={
            "mensagem": Mensagem.objects.get(idmensagem=idmensagem),
            "professores": Professor.objects.all()
        }
    if request.method == 'POST':
        mensagem = Mensagem.objects.get(idmensagem=idmensagem)
        if request.sessao.usuario.profile == 'P':
            mensagem.status = "RESPONDIDO"
            mensagem.dtresposta=time.strftime("%Y-%m-%d")
            mensagem.resposta = request.POST.get("resposta")
            mensagem.save()
            return redirect('listarmensagensprofessores')            
        return redirect('listarmensagensprofessores')

    else:
        return render(request, "formNovaMensagem.html",context )

def deletarEntrega(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno
  
    return redirect ('listaratividadevinculada')