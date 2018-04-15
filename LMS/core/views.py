from django.shortcuts import render
from django.http import HttpResponse
<<<<<<< HEAD
from .utils.utils import calculaMediaFinal
=======
from core.utils.utils import calculaMediaFinal
>>>>>>> origin/pablo


def index(request):
    return render(request, "index.html")



# def index(request):
    # return HttpResponse('Login')
#    return HttpResponse(calculaMediaFinal(10, 5))


def login(request):
<<<<<<< HEAD
    if request.method == "GET":
        return render(request, "login.html")
    else:
        user = request.POST.get("email")
        if request.POST.get("senha") != "teste123":
            print("Usuário {0} digitou senha errada" .format(user))
            # A função render não redireciona -- veja essa função
            # https://docs.djangoproject.com/en/2.0/topics/http/shortcuts/#redirect
            return render(request, "login.html")
        else:
            print("Usuário {0} entrou com sucesso" .format(user))
            return render(request, "index.html")


def contato(request):
    if request.method == "GET":
        return render(request, "contato.html")
    else:
        print(request.POST.get("nome"))
        print(request.POST.get("email"))
        print(request.POST.get("assunto"))
        print(request.POST.get("Mensagem"))
        print(request.POST.get("telefone"))
    return render(request, "contato.html")
    
   
=======
    return render(request, "login.html")


def templateBase(request):
    return render(request, "base.html")


def novoAluno(request):
    return render(request, "Formulario_Novo_Aluno.html")


def cursos(request):
    return render(request, "cursos.html")


def detalheCurso(request):
    return render(request, "detalhe_curso.html")


def detalheDisciplina(request):
    return render(request, "detalhes_disciplina.html")


def formularioCurso(request):
    return render(request, "formulario_curso.html")


def formularioDisciplina(request):
    return render(request, "formulario_disciplina.html")


def formularioMatricula(request):
    return render(request, "formulario_matricula.html")


def painelAdmin(request):
    return render(request, "painel_admin.html")
>>>>>>> origin/pablo
