from django.shortcuts import render, redirect
from .models import Professor



def listarProfessores(request):
    professores = Professor.objects.all()
    return render(request, 'listaProfessores.html', {'professores': professores})

def inserirProfessor(request):
    context = {}
    if request.method == 'POST':
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
        return render(request, 'formNovoProfessor.html', context)

def alterarProfessor(request, idprofessor):
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
        return render(request, 'formNovoProfessor.html', {'professor':professor})


def deletarProfessor(request, idprofessor):
    professores = Professor.objects.get(idprofessor=idprofessor)
    professores.delete()
    return redirect ('listarprofessores')