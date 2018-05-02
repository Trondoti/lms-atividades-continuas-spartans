from django.shortcuts import render, redirect
from .models import Curso, Disciplina
from contas.models import Coordenador


def listarCursos(request):
    cursos = Curso.objects.all()
    return render(request, 'listaCursos.html', {'cursos': cursos})

def inserirCurso(request):
    context = {}
    if request.method == 'POST':
        Curso.objects.create (
            nome=request.POST.get("curso")
        )        
        return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", context)

def alterarCurso(request, idcurso):
    cursos = Curso.objects.get(idcurso=idcurso)
    context = {"cursos":cursos}
    if request.method == 'POST':
       curso = Curso.objects.get(idcurso=idcurso)
       curso.nome = request.POST.get('curso')
       curso.save()
       return redirect('listarcursos')
    else:
        return render(request, "formNovoCurso.html", {'cursos':cursos})


def deletarCurso(request, idcurso):
    curso = Curso.objects.get(idcurso=idcurso)
    curso.delete()
    return redirect ('listarcursos')
    
def listarDisciplinas(request):
    contexto = {
        "disciplinas":Disciplina.objects.all()
    }
    return render(request, 'listaDisciplinas.html', contexto)

def inserirDisciplina(request):
    coordenadores ={'coordenadores':Coordenador.objects.all()}
    if request.method == 'POST':
        idcoordenador = Coordenador.objects.get(idcoordenador = request.POST.get("coordenador"))
        Disciplina.objects.create (
            nome=request.POST.get("nome"),
            data = request.POST.get("data"),
            statusdisc = request.POST.get("status"),
            planodeensino = request.POST.get("plano"),
            cargahoraria = request.POST.get("carga_horaria"),
            competencias = request.POST.get("competencias"),
            habilidades = request.POST.get("habilidades"),
            ementa = request.POST.get("ementa"),
            conteudoprogramatico = request.POST.get("conteudo"),
            bibliografiabasica = request.POST.get("bbasica"),
            bibliografiacomplementar = request.POST.get("bcomplementar"),
            percentualpratico = request.POST.get("ppratico"),
            percentualteorico = request.POST.get("pteorico"),
            idcoordenador = idcoordenador
        )
        return redirect('listardisciplinas')
    else:
        return render(request, "formNovaDisciplina.html", coordenadores)

def alterarDisciplina(request, idcurso):
    cursos = Curso.objects.get(idcurso=idcurso)
    context = {"cursos":cursos}
    if request.method == 'POST':
       curso = Curso.objects.get(idcurso=idcurso)
       curso.nome = request.POST.get('curso')
       curso.save()
       return redirect('listardisciplinas')
    else:
        return render(request, "formNovoCurso.html", {'cursos':cursos})


def deletarDisciplina(request, idcurso):
    curso = Curso.objects.get(idcurso=idcurso)
    curso.delete()
    return redirect ('listardisciplinas')
