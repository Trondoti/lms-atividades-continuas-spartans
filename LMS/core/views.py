from django.shortcuts import render
from django.http import HttpResponse
from core.utils.utils import calculaMediaFinal


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def templateBase(request):
    return render(request, "base.html")


def novoAluno(request):
    return render(request, "Formulario_Novo_Aluno.html")


def cursos(request):
    context = {
        'curso' : ["Analise e desenvolvimento","Ciência da computação", "Sistema de informação"],
        'curso2': ["Banco de dados", "Jogos Digitais", "Redes de computadores"],
        'urls': ["detalhe-curso-bd", "detalhe-curso-ads"]
        
            }
    return render(request, "cursos.html", context)
    


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
