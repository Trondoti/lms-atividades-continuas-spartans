from django.core.exceptions import ObjectDoesNotExist
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from core.models.sessao import Sessao

def autenticar(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    try:
        try:
            login = Professor.objects.get(email=email)
        except:
            try:
                login = Coordenador.objects.get(email=email)
            except:
                try:
                    login = Aluno.objects.get(email=email)
                except:
                    return False
        if login.senha == senha:
            if(login.__class__.__name__ == "Aluno"):
                sessao = Sessao.objects.create(idaluno = login)
                request.sessao = sessao
                return True
            elif(login.__class__.__name__ == "Professor"):
                sessao = Sessao.objects.create(idprofessor = login)
                request.sessao = sessao
                return True
            elif(login.__class__.__name__ == "Coordenador"):
                sessao = Sessao.objects.create(idcoordenador = login)
                request.sessao = sessao
                return True
            return False
        else:
            return False
    except ObjectDoesNotExist:
        return False
