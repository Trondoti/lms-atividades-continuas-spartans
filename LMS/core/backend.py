from django.core.exceptions import ObjectDoesNotExist
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador


def autenticar(request):
    email = request.POST.get("email")
    senha = request .POST.get("senha")
    try:         
        login1 = Professor.objects.get(email=email)
        login2 = Coordenador.objects.get(email=email)
        login3 = Aluno.objects.get(email=email)
        if login.senha == senha or login2.senha == senha or login3.senha == senha:
            return True
        else:
            return False
    except ObjectDoesNotExist:
        return False
