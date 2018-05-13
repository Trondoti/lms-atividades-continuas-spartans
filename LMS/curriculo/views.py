from django.shortcuts import render, redirect
from .models.curso import Curso
from .models.disciplina import Disciplina
from .models.disciplinaOfertada import Disciplinaofertada
from contas.models.coordenador import Coordenador
from contas.models.professor import Professor
from restrito.models.atividade import Atividade

def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listaCursos.html', {'cursos': cursos})

def inserirCurso(request):
    context = {}
    if request.method == 'POST':
        Curso.objects.create(
            nome=request.POST.get("curso")
        )
        return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", context)

def alterarCurso(request, idcurso):
    cursos = Curso.objects.get(idcurso=idcurso)
    context = {"cursos": cursos}
    if request.method == 'POST':
        curso = Curso.objects.get(idcurso=idcurso)
        curso.nome = request.POST.get('curso')
        curso.save()
        return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", {'cursos': cursos})

def deletarCurso(request, idcurso):
    curso = Curso.objects.get(idcurso=idcurso)
    curso.delete()
    return redirect('listarcursos')

def listarDisciplinas(request):
    contexto = {
        "disciplinas": Disciplina.objects.all()
    }
    return render(request, 'listaDisciplinas.html', contexto)

def inserirDisciplina(request):
    contexto = {'coordenadores': Coordenador.objects.all()}
    if request.method == 'POST':
        idcoordenador = Coordenador.objects.get(
            idcoordenador=request.POST.get("coordenador"))
        Disciplina.objects.create(
            nome=request.POST.get("nome"),
            data=request.POST.get("data"),
            statusdisc=request.POST.get("statusdisc"),
            planodeensino=request.POST.get("plano"),
            cargahoraria=request.POST.get("cargahoraria"),
            competencias=request.POST.get("competencias"),
            habilidades=request.POST.get("habilidades"),
            ementa=request.POST.get("ementa"),
            conteudoprogramatico=request.POST.get("conteudoprogramatico"),
            bibliografiabasica=request.POST.get("bibliografiabasica"),
            bibliografiacomplementar=request.POST.get("bibliografiacomplementar"),
            percentualpratico=request.POST.get("percentualpratico"),
            percentualteorico=request.POST.get("percentualteorico"),
            idcoordenador=idcoordenador
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplina.html", contexto)

def alterarDisciplina(request, iddisciplina):
    if request.method == 'POST':
        idcoordenador = Coordenador.objects.get(idcoordenador=request.POST.get("coordenador"))
        disciplina = Disciplina.objects.get(iddisciplina=iddisciplina)
        disciplina.nome = request.POST.get("nome"),
        disciplina.data = request.POST.get("data"),
        disciplina.statusdisc = request.POST.get("statusdisc"),
        disciplina.planodeensino = request.POST.get("plano"),
        disciplina.cargahoraria = request.POST.get("cargahoraria"),
        disciplina.competencias = request.POST.get("competencias"),
        disciplina.habilidades = request.POST.get("habilidades"),
        disciplina.ementa = request.POST.get("ementa"),
        disciplina.conteudoprogramatico = request.POST.get("conteudoprogramatico"),
        disciplina.bibliografiabasica = request.POST.get("bibliografiabasica"),
        disciplina.bibliografiacomplementar = request.POST.get("bibliografiacomplementar"),
        disciplina.percentualpratico = request.POST.get("percentualpratico"),
        disciplina.percentualteorico = request.POST.get("percentualteorico"),
        disciplina.idcoordenador = idcoordenador
        disciplina.save()
        return redirect('listardisciplinas')
    else:
        contexto = {
            'coordenadores': Coordenador.objects.all(),
            'disciplina': Disciplina.objects.get(iddisciplina=iddisciplina)
        }
        return render(request, "formNovaDisciplina.html", contexto)

def deletarDisciplina(request, iddisciplina):
    disciplina = Disciplina.objects.get(iddisciplina=iddisciplina)
    disciplina.delete()
    return redirect('listardisciplinas')

def listarDisciplinasOfertadas(request):
    contexto = {
        "atividades":Atividadevinculada.objects.all()
    }
    return render(request, 'listarDisciplinas.html', contexto)

def inserirDisciplinaOfertada(request, iddisciplina):
    contexto ={
        'professores':Professor.objects.all(),
        'disciplina': Disciplina.objects.get(iddisciplina=iddisciplina),
        'cursos': Curso.objects.all(),
    }
    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        curso = Curso.objects.get(idcurso=request.POST.get("curso"))
        coordenador = Coordenador.objects.get(idcoordenador=request.POST.get("coordenador"))
        disciplina = Disciplina.objects.get(iddisciplina = iddisciplina)
        Disciplinaofertada.objects.create(
            idcoordenador=coordenador,
            dtiniciomatricula = request.POST.get("dtiniciomatricula"),
            dtfimmatricula = request.POST.get("dtfimmatricula"),
            iddisciplina=disciplina,
            idcurso=curso,
            ano=request.POST.get("ano"),
            semestre=request.POST.get("semestre"),
            idprofessor=professor,
            metodologia=request.POST.get("metodologia"),
            recursos = request.POST.get("recursos"),
            criterioavaliacao = request.POST.get("criterios"),
            planodeaulas = request.POST.get("plano")
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplinaOfertada.html", contexto)

def alterarDisciplinaOfertada(request, idatividadevinculada):
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
        return redirect('listaratividadesvinculadas')
    else:
        contexto ={
            'professores':Professor.objects.all(),
            'atividades': Atividade.objects.all(),
            'disciplinas': Disciplina.objects.all(),
            'disciplinaofertada':
            'atividadevinculada':Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
        }
    return render(request, "formNovaAtividadeVinculada.html", contexto)

def deletarDisciplinaOfertada(request, idatividadevinculada):
    atividadevinculada = Atividadevinculada.objects.get(idatividadevinculada=idatividadevinculada)
    atividadevinculada.delete()
    return redirect ('listaratividadesvinculadas')
