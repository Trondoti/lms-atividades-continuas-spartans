from django.core.exceptions import ObjectDoesNotExist
from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from .loginHelper import LoginHelper


def autenticar(request):
    email = request.POST.get("email")
    senha = request.POST.get("senha")
    l = LoginHelper()
    usuario = l.montarLogin(email)

    if usuario.statusCode == 200:
        if usuario.senha == senha:
            l.salvarSessao(usuario)
            return True
        else:
            return False
