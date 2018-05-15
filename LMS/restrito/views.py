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
import time

def listarAtividades(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaAtividades.html', {"atividades": Atividade.objects.all()})

def inserirAtividade(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.sessao.usuario.id)

        Atividade.objects.create (
            titulo=request.POST.get("titulo"),
            descricao = request.POST.get("descricao"),
            conteudo = request.POST.get("conteudo"),
            tipo = request.POST.get("tipo"),
            extra = request.POST.get("extra"),
            idprofessor = professor
        )
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividade.html")

def alterarAtividade(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        atividade = Atividade.objects.get(idatividade=idatividade)
        atividade.titulo=request.POST.get("titulo")
        atividade.descricao = request.POST.get("descricao")
        atividade.conteudo = request.POST.get("conteudo")
        atividade.tipo = request.POST.get("tipo")
        atividade.extra = request.POST.get("extra")
        atividade.save()
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividade.html", {'atividade': Atividade.objects.get(idatividade=idatividade)})

def deletarAtividade(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividade = Atividade.objects.get(idatividade=idatividade)
    atividade.delete()
    return redirect ('listaratividades')

def listarAtividadeVinculada(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaAtividadesVinculadas.html', {"atividades": Atividadevinculada.objects.all()})

def inserirAtividadeVinculada(request, idatividade):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    contexto = {
        'atividade': Atividade.objects.get(idatividade=idatividade),
        'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y"))),
    }

    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.sessao.usuario.id)
        atividade = Atividade.objects.get(idatividade=idatividade)
        disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplinaofertada"))
        Atividadevinculada.objects.create(
            idprofessor=professor,
            idatividade=atividade,
            iddisciplinaofertada=disciplinaofertada,
            rotulo=request.POST.get("rotulo"),
            estado=request.POST.get("estado"),
            dtiniciorespostas=request.POST.get("dtiniciorespostas"),
            dtfimrespostas=request.POST.get("dtfimrespostas")
        )
        return redirect('listaratividades')
    else:
        return render(request, "formNovaAtividadeVinculada.html", contexto)

def alterarAtividadeVinculada(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        atividadevindulada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=request.POST.get("disciplinaofertada"))
        atividadevindulada.iddisciplinaofertada = disciplinaofertada
        atividadevindulada.rotulo = request.POST.get("rotulo")
        atividadevindulada.estado = request.POST.get("estado")
        atividadevindulada.dtiniciorespostas = request.POST.get("dtiniciorespostas")
        atividadevindulada.dtfimrespostas = request.POST.get("dtfimrespostas")
        atividadevindulada.save()
        return redirect('listaratividadevinculada')
    else:
        atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        contexto ={
            'atividade': atividadevinculada.idatividade,
            'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y"))),
            'atividadevinculada': atividadevinculada
        }
        return render(request, "formNovaAtividadeVinculada.html", contexto)

def deletarAtividadeVinculada(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')

def listarEntregasAlunos(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasAlunos.html', {"entregas": Entrega.objects.filter(idaluno=request.sessao.usuario.id)})

def listarEntregasProfessores(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaEntregasProfessores.html', {"entregas": Entrega.objects.filter(idatividadevinculada__idprofessor=request.sessao.usuario.id)})

def inserirEntrega(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        idatividade = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id)
        Entrega.objects.create(
            idaluno=idaluno,
            titulo=request.POST.get("titulo"),
            resposta=request.POST.get("resposta"),
            idatividadevinculada=idatividade,
            dtentrega=time.strftime("%Y-%m-%d"),
            status="ENTREGUE"
        )
        return redirect('listarentregas')
    else:
        return render(request, "formNovaEntrega.html")

def alterarEntrega(request, identrega):
    try:
        if request.sessao.usuario.profile != "A" and request.sessao.usuario.profile != 'P':
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        entrega = Entrega.objects.get(identrega=identrega)
        entrega.titulo=request.POST.get("titulo")
        entrega.resposta=request.POST.get("resposta")
        entrega.dtentrega=time.strftime("%Y-%m-%d")
        if request.sessao.usuario.profile == 'P':
            entrega.nota = request.POST.get("nota")
            entrega.obs = request.POST.get("observacao")
            entrega.dtavaliacao=time.strftime("%Y-%m-%d")
            entrega.save()
            return redirect('listarentregasprofessores')
        entrega.save()
        return redirect('listarentregasalunos')

    else:
        return render(request, "formNovaEntrega.html", {'entrega': Entrega.objects.get(identrega=identrega)})

def deletarEntrega(request, idatividadevinculada):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadevinculada')

def listarSolicitacaoMatricula(request):
    try:
        if request.sessao.usuario.profile != "P":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    return render(request, 'listaSolicitacaoMatricula.html', {"solicitacoes": Solicitacaomatricula.objects.filter(status="SOLICITADA")})

def inserirSolicitacaoMatricula(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        for matricula in request.POST.getlist("matricula"):
            Solicitacaomatricula.objects.create (
                idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id),
                iddisciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=matricula),
                dtsolicitacao=time.strftime("%Y-%m-%d"),
                status = "SOLICITADA",
            )
        return redirect('aluno')
    else:
        return render(request, 'formNovaSolicitacaoMatricula.html', {'disciplinasofertadas': Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y")))})

def alterarSolicitacao(request):
    try:
        if request.sessao.usuario.profile != "C":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    if request.method == 'POST':
        solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
        arrantigo = []
        for sm in solicitacaomatricula:
            arrantigo.append(sm.iddisciplinaofertada.iddisciplinaofertada)

        arrnovo = []
        for matricula in request.POST.getlist("matricula"):
            arrnovo.append(matricula)

        if not (arrantigo==arrnovo):
            for sm in solicitacaomatricula:
                sm.delete()

            for matricula in request.POST.getlist("matricula"):
                Solicitacaomatricula.objects.create (
                    idaluno = Aluno.objects.get(idaluno=request.sessao.usuario.id),
                    iddisciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=matricula),
                    dtsolicitacao=time.strftime("%Y-%m-%d"),
                    status = "SOLICITADA",
                )

        return redirect('alterarsolicitacao')
    else:
        solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
        disciplinasofertadas = Disciplinaofertada.objects.filter(ano=int(time.strftime("%Y")));
        for disciplinaofertada in disciplinasofertadas:
            if any(sm.iddisciplinaofertada.iddisciplinaofertada == disciplinaofertada.iddisciplinaofertada for sm in solicitacaomatricula):
                disciplinaofertada.selected = True
            else:
                disciplinaofertada.selected = False

        return render(request, "formNovaSolicitacaoMatricula.html", {'disciplinasofertadas': disciplinasofertadas})

def deletarSolicitacao(request):
    try:
        if request.sessao.usuario.profile != "A":
            return redirect("/")
    except:
        retorno = redirect("/")
        retorno.delete_cookie("SPARTANSSESSION")
        return retorno

    solicitacaomatricula = Solicitacaomatricula.objects.filter(idaluno=request.sessao.usuario.id, status="SOLICITADA")
    solicitacaomatricula.delete()
    return redirect ('inserirsolicitacao')


def aprovarSolicitacao(request):
    i
    return render(request, 'formAprovarSolicitacao.html', {"solicitacoes": Solicitacaomatricula.objects.filter(status="SOLICITADA")})
