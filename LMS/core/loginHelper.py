from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador


class LoginHelper():

    def montarLogin(self, email):
        usuario = {
            "statusCode": ""
        }

        try:
            professor = Professor.objects.get(email=email)
            usuario.statusCode = 200
            usuario.profile = "P"
            usuario.id = professor.idprofessor
            usuario.nome = professor.nome
            return usuario
        except:
            try:
                coordenador = Coordenador.objects.get(email=email)
                usuario.statusCode = 200
                usuario.profile = "C"
                usuario.id = coordenador.idcoordenador
                usuario.nome = coordenador.nome
                return usuario
            except:
                try:
                    aluno = Aluno.objects.get(email=email)
                    usuario.statusCode = 200
                    usuario.profile = "A"
                    usuario.id = aluno.idaluno
                    usuario.nome = aluno.nome
                    return usuario
                except:
                    usuario.statusCode = 404
                    return usuario

    def salvarSessao(self, usuario):
        if(usuario.profile == "A"):
            Session.objects.create(
                idaluno = usuario.id
            )
        if(usuario.profile == "C"):
            Session.objects.create(
                idcoordenador = usuario.id
            )
        if(usuario.profile == "P"):
            Session.objects.create(
                idprofessor = usuario.id
            )
        
