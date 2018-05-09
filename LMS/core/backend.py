from django.core.exceptions import ObjectDoesNotExist
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador


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
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False
