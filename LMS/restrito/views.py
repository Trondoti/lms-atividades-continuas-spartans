from django.shortcuts import render, redirect
from .models.atividade import Atividade
from curriculo.models.disciplina import Disciplina
from curriculo.models.disciplinaOfertada import Disciplinaofertada
from .models.atividadeVinculada import Atividadevinculada
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from restrito.models.solicitacaoMatricula import Solicitacaomatricula
from .models.entrega import Entrega
    
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
        idprofessor = Professor.objects.get(idprofessor = request.POST.get("professor"))
        atividade = Atividade.objects.get(idatividade=idatividade)
        atividade.titulo=request.POST.get("titulo")
        atividade.descricao = request.POST.get("descricao")
        atividade.conteudo = request.POST.get("conteudo")
        atividade.tipo = request.POST.get("tipo")
        atividade.extra = request.POST.get("extra")
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


   
def listarAtividadeVinculada(request):
    contexto = {
        "atividades":Atividadevinculada.objects.all()
    }
    return render(request, 'listaAtividadesVinculadas.html', contexto)


def inserirAtividadeVinculada(request):
    contexto ={
        'professores':Professor.objects.all(),
        'atividades': Atividade.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        
    }
    if request.method == 'POST':
        idprofessor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        idatividade = Atividade.objects.get(idatividade=request.POST.get("atividade"))
        iddisciplina = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplina"))
        Atividadevinculada.objects.create(
            idprofessor=idprofessor,
            idatividade=idatividade,
            iddisciplinaofertada=iddisciplina,
            rotulo=request.POST.get("rotulo"),
            estado=request.POST.get("estado"),
            dtiniciorespostas=request.POST.get("dtiniciorespostas"),
            dtfimrespostas=request.POST.get("dtfimrespostas")
        )
        return redirect('listaratividadevinculada')
    else:
        return render(request, "formNovaAtividadeVinculada.html", contexto)

def alterarAtividadeVinculada(request, idatividadevinculada):
    if request.method == 'POST':
        atividadevindulada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        idprofessor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        idatividade = Atividade.objects.get(idatividade=request.POST.get("atividade"))
        iddisciplina = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplina"))
        atividadevindulada.idprofessor = idprofessor,
        atividadevindulada.idatividade = atividade,
        atividadevindulada.iddisciplinaofertada = disciplina,
        atividadevindulada.rotulo = request.POST.get("rotulo"),
        atividadevindulada.estado = request.POST.get("estado"),
        atividadevindulada.dtiniciorespostas = request.POST.get("dtiniciorespostas"),
        atividadevindulada.dtfimrespostas = request.POST.get("dtfimrespostas")
        atividadevindulada.save()
        return redirect('listaratividadevinculada')
    else:
        contexto ={
        'professores':Professor.objects.all(),
        'atividades': Atividade.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        'atividadevinculada':Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        
    }
        return render(request, "formNovaAtividadeVinculada.html", contexto)


def deletarAtividadeVinculada(request, idatividadevinculada):
    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')


def listarEntregas(request):
    contexto = {
        "entregas":Entrega.objects.all()
    }
    return render(request, 'listaEntregas.html', contexto)


def inserirEntrega(request):
    contexto ={
        'professores':Professor.objects.all(),
        'atividades': Atividade.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        'alunos': Aluno.objects.all(),
        'atividadesvinculadas': Atividadevinculada.objects.all(),
        
    }
    if request.method == 'POST':
        idprofessor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        idatividade = Atividadevinculada.objects.get(idatividadevinculada=request.POST.get("atividadevinculada"))
        idaluno = Aluno.objects.get(idaluno=request.POST.get("aluno"))
        Entrega.objects.create(
            idaluno=idaluno,
            titulo=request.POST.get("titulo"),
            resposta=request.POST.get("resposta"),
            idatividadevinculada=idatividade,
            idprofessor=idprofessor,
           
        )
        return redirect('listarentregas')
    else:
        return render(request, "formNovaEntrega.html", contexto)

def alterarEntrega(request, identrega):
    if request.method == 'POST':
        idprofessor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        idatividade = Atividadevinculada.objects.get(idatividadevinculada=request.POST.get("atividadevinculada"))
        idaluno = Aluno.objects.get(idaluno=request.POST.get("aluno"))
        entrega = Entrega.objects.get(identrega=identrega)
        entrega.idaluno=idaluno,
        entrega.titulo=request.POST.get("titulo"),
        entrega.resposta=request.POST.get("resposta"),
        entrega.idatividadevinculada=idatividade,
        entrega.idprofessor=idprofessor,
        entrega.save()
        return redirect('listarentregas')
    else:
        contexto ={
        'professores':Professor.objects.all(),
        'atividades': Atividade.objects.all(),
        'disciplinas': Disciplina.objects.all(),
        'alunos': Aluno.objects.all(),
        'atividadesvinculadas': Atividadevinculada.objects.all(),
               }
        return render(request, "formNovaEntrega.html", contexto)


def deletarEntrega(request, idatividadevinculada):
    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')

def listarSolicitacaoMatricula(request):
    contexto = {
        "solicitacoes":Solicitacaomatricula.objects.all()
    }
    return render(request, 'listaSolicitacaoMatricula.html', contexto)

def inserirSolicitacaoMatricula(request):
    context = {
        'alunos':Aluno.objects.all(),
        'disciplinaofertadas': Disciplinaofertada.objects.all(),
        'coordenadores': Coordenador.objects.all(),
                
    }
    if request.method == 'POST':
        Solicitacaomatricula.objects.create (
        idaluno = Aluno.objects.get(idaluno=request.POST.get("idAluno")),
        iddisciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("idDisciplinaOfertada")),
        dtsolicitacao = request.POST.get('dtSolicitacao'),
        idcoordenador = Coordenador.objects.get(idcoordenador=request.POST.get("idCoordenador")),
        status = request.POST.get('status'),
        )        
        return redirect('listarsolicitacao')
    else:
        return render(request, 'formNovaSolicitacaoMatricula.html', context)

def alterarSolicitacao(request,idsolicitacaomatricula):
    if request.method == 'POST':
        solicitacaomatricula = Solicitacaomatricula.objects.get(idsolicitacaomatricula=idsolicitacaomatricula)
        aluno = Aluno.objects.get(idaluno=request.POST.get("idAluno"))
        disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("idDisciplinaOfertada"))
        coordenador = Coordenador.objects.get(idcoordenador=request.POST.get("idCoordenador"))
        solicitacaomatricula.idaluno = aluno
        solicitacaomatricula.iddisciplinaofertada = disciplinaofertada        
        solicitacaomatricula.status = request.POST.get('status')
        solicitacaomatricula.dtsolicitacao = request.POST.get('dtSolicitacao')
        solicitacaomatricula.idcoordenador = coordenador
        solicitacaomatricula.save()
        return redirect('listarsolicitacao')
    else:
        contexto ={
        'alunos':Aluno.objects.all(),
        'coordenadores': Coordenador.objects.all(),
        'disciplinaofertadas': Disciplinaofertada.objects.all(),
        'solicitacao' : Solicitacaomatricula.objects.get(idsolicitacaomatricula=idsolicitacaomatricula),
               }
        return render(request, "formNovaSolicitacaoMatricula.html", contexto)

def deletarSolicitacao(request, idsolicitacaomatricula):
    solicitacaomatricula = Solicitacaomatricula.objects.get(idsolicitacaomatricula=idsolicitacaomatricula)
    solicitacaomatricula.delete()
    return redirect ('listarsolicitacao')