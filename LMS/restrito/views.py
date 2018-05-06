from django.shortcuts import render, redirect
from .models.atividade import Atividade
from contas.models.professor import Professor
    
def listarAtividades(request):
    contexto = {
        "atividades":Atividade.objects.all()
    }
    return render(request, 'listaAtividades.html', contexto)


def inserirAtividade(request):
    contexto ={'professores':Professor.objects.all()}
    if request.method == 'POST':
        idprofessor = Professor.objects.get(idprofessor = request.POST.get("professor"))
        Atividade.objects.create (
            titulo=request.POST.get("titulo"),
            descricao = request.POST.get("descricao"),
            conteudo = request.POST.get("conteudo"),
            tipo = request.POST.get("tipo"),
            extra = request.POST.get("extra"),
            idprofessor = idprofessor
        )
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividade.html", contexto)

def alterarAtividade(request, idatividade):
    if request.method == 'POST':
        idprofessor = Coordenador.objects.get(idprofessor = request.POST.get("professor"))
        atividade = Atividade.objects.get(idatividade=idatividade)
        atividade.titulo=request.POST.get("titulo"),
        atividade.descricao = request.POST.get("descricao"),
        atividade.conteudo = request.POST.get("conteudo"),
        atividade.tipo = request.POST.get("tipo"),
        atividade.extra = request.POST.get("extra"),
        idprofessor = idprofessor
        atividade.professor = idprofessor
        atividade.save()
        return redirect('listaratividades')
    else:
        contexto ={
        'professores':Professor.objects.all(),
        'atividade':Atividade.objects.get(idatividade=idatividade)
        }
        return render(request, "formNovaAtividade.html", contexto)


def deletarAtividade(request, idatividade):
    atividade = Atividade.objects.get(idatividade=idatividade)
    atividade.delete()
    return redirect ('listaratividades')