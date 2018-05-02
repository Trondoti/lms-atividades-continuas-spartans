from django.shortcuts import render, redirect
from .models import Aluno, Coordenador
import base64
import hashlib

def listarAlunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'listaAlunos.html', { 'alunos' : alunos })

def inserirAluno(request):
    if request.method == 'POST':

        file = request.FILES['foto']
        encoded = base64.b64encode(file.read())
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()
        print(senha);
        Aluno.objects.create (
            logon=request.POST.get("logon"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular"),
            foto=encoded
        )

        return redirect('listarAlunos')
    else:
        return render(request, "formNovoAluno.html")

def alterarAluno(request, idaluno):
    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.foto = aluno.foto[2:-1]


    if request.method == 'POST':
        file = request.FILES['foto']
        encoded = base64.b64encode(file.read())
        #senha = hashlib.sha224(request.POST.get("senha").encode('utf-8')).hexdigest()

        aluno = Aluno.objects.get(idaluno=idaluno)
        logon=request.POST.get("logon")
        senha=request.POST.get("senha")
        nome=request.POST.get("nome")
        email=request.POST.get("email")
        celular=request.POST.get("celular")
        foto=encoded
        aluno.save()
        return redirect('listarAlunos')
    else:
        return render(request, "formNovoAluno.html", { "aluno" : aluno })

def deletarAluno(request, idaluno):
    aluno = Aluno.objects.get(idaluno=idaluno)
    aluno.delete()
    return redirect ('listarAlunos')

def listarCoordenadores(request):
    coordenadores = Coordenador.objects.all()
    return render(request, 'listarCoordenadores.html', {'coordenadores': coordenadores})

def inserirCoordenador(request):
    if request.method == 'POST':
        Coordenador.objects.create (
            logon=request.POST.get("logon"),
            senha=request.POST.get("senha"),
            nome=request.POST.get("nome"),
            email=request.POST.get("email"),
            celular=request.POST.get("celular")
        )
        return redirect('listarCoordenadores')
    else:
        return render(request, "formNovoCoordenador.html")

def alterarCoordenador(request, idcoordenador):
    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    if request.method == 'POST':
        coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
        coordenador.logon=request.POST.get("logon")
        coordenador.senha=request.POST.get("senha")
        coordenador.nome=request.POST.get("nome")
        coordenador.email=request.POST.get("email")
        coordenador.celular=request.POST.get("celular")
        coordenador.save()
        return redirect('listarCoordenadores')
    else:
        return render(request, "formNovoCoordenador.html", { "coordenador" : coordenador })

def deletarCoordenador(request, idcoordenador):
    coordenador = Coordenador.objects.get(idcoordenador=idcoordenador)
    coordenador.delete()
    return redirect ('listarCoordenadores')
