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
            statusdisc=request.POST.get("status"),
            planodeensino=request.POST.get("plano"),
            cargahoraria=request.POST.get("carga_horaria"),
            competencias=request.POST.get("competencias"),
            habilidades=request.POST.get("habilidades"),
            ementa=request.POST.get("ementa"),
            conteudoprogramatico=request.POST.get("conteudo"),
            bibliografiabasica=request.POST.get("bbasica"),
            bibliografiacomplementar=request.POST.get("bcomplementar"),
            percentualpratico=request.POST.get("ppratico"),
            percentualteorico=request.POST.get("pteorico"),
            idcoordenador=idcoordenador
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplina.html", contexto)


def alterarDisciplina(request, iddisciplina):
    if request.method == 'POST':
        idcoordenador = Coordenador.objects.get(
        idcoordenador=request.POST.get("coordenador"))
        disciplina.nome = request.POST.get("nome"),
        disciplina.data = request.POST.get("data"),
        disciplina.statusdisc = request.POST.get("status"),
        disciplina.planodeensino = request.POST.get("plano"),
        disciplina.cargahoraria = request.POST.get("carga_horaria"),
        disciplina.competencias = request.POST.get("competencias"),
        disciplina.habilidades = request.POST.get("habilidades"),
        disciplina.ementa = request.POST.get("ementa"),
        disciplina.conteudoprogramatico = request.POST.get("conteudo"),
        disciplina.bibliografiabasica = request.POST.get("bbasica"),
        disciplina.bibliografiacomplementar = request.POST.get("bcomplementar"),
        disciplina.percentualpratico = request.POST.get("ppratico"),
        disciplina.percentualteorico = request.POST.get("pteorico"),
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
        "disciplinasofertadas":Disciplinaofertada.objects.all()
    }
    return render(request, 'listarDisciplinasOfertadas.html', contexto)


def inserirDisciplinaOfertada(request, iddisciplina):
    contexto ={
        'professores':Professor.objects.all(),
        'atividade': Atividade.objects.all(),
        'disciplina': Disciplina.objects.get(iddisciplina=iddisciplina),
        'coordenadores': Coordenador.objects.all(),
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
            turma=request.POST.get("turma"),
            idprofessor=professor,
            metodologia=request.POST.get("metodologia"),
            recursos = request.POST.get("recursos"),
            criterioavaliacao = request.POST.get("criterios"),
            planodeaulas = request.POST.get("planodeaulas")
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplinaOfertada.html", contexto)

def alterarDisciplinaOfertada(request, iddisciplinaofertada):
    if request.method == 'POST':
        professor = Professor.objects.get(idprofessor=request.POST.get("professor"))
        curso = Curso.objects.get(idcurso=request.POST.get("curso"))
        do = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
        do.dtiniciomatricula = request.POST.get("dtiniciomatricula")
        do.dtfimmatricula = request.POST.get("dtfimmatricula")
        do.iddisciplina=do.iddisciplina
        do.idcurso=curso
        do.ano=request.POST.get("ano")
        do.semestre=request.POST.get("semestre")
        do.turma=request.POST.get("turma")
        do.idprofessor=professor
        do.metodologia=request.POST.get("metodologia")
        do.recursos = request.POST.get("recursos")
        do.criterioavaliacao = request.POST.get("criterios")
        do.planodeaulas = request.POST.get("plano")
        do.save()
        return redirect('listardisciplinasofertadas')
    else:
        do = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
        contexto ={
        'professores':Professor.objects.all(),
        'atividades': Atividade.objects.all(),
        'disciplinaofertada': Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada),
        'cursos': Curso.objects.all(),
        'disciplina': do.iddisciplina
        }
        return render(request, "formNovaDisciplinaOfertada.html", contexto)


def deletarDisciplinaOfertada(request, iddisciplinaofertada):
    disciplinaofertada = Disciplinaofertada.objects.get(iddisciplinaofertada=iddisciplinaofertada)
    disciplinaofertada.delete()
    return redirect ('listardisciplinasofertadas')