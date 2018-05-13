from contas.models.professor import Professor
from contas.models.aluno import Aluno
from contas.models.coordenador import Coordenador
from core.models.sessao import Sessao
from core.models.usuario import Usuario

class LoginHelper():

    def montarUsuario(self, email):

        try:
            professor = Professor.objects.get(email=email)
            return Usuario(200, "P", professor.idprofessor, professor.logon, professor.nome, professor.senha, professor.email, professor.celular, professor.dtexpiracao)
        except:
            try:
                coordenador = Coordenador.objects.get(email=email)
                return Usuario(200, "C", coordenador.idcoordenador, coordenador.logon, coordenador.nome, coordenador.senha, coordenador.email, coordenador.celular, coordenador.dtexpiracao)
            except:
                try:
                    aluno = Aluno.objects.get(email=email)
                    return  Usuario(200, "A", aluno.idaluno, aluno.logon, aluno.nome, aluno.senha, aluno.email, aluno.celular, aluno.dtexpiracao)
                except:
                    return Usuario(404, None, None, None, None, None, None, None, None)


    def salvarSessao(self, usuario):
        if(usuario.profile == "A"):
            aluno = Aluno.objects.get(idaluno=usuario.id)

            return Sessao.objects.create(
                idaluno = aluno
            )
        if(usuario.profile == "C"):
            coordenador = Coordenador.objects.get(idcoordendaor=usuario.id)

            return Sessao.objects.create(
                idcoordenador = coordenador
            )
        if(usuario.profile == "P"):
            professor = Professor.objects.get(idprofessor=usuario.id)

            return Sessao.objects.create(
                idprofessor = professor
            )

    def pegarUsuarioPelaSessao(self, sessao):
        try:
            return self.montarUsuario(sessao.idaluno.email)
        except:
            try:
                return self.montarUsuario(sessao.idcoordenador.email)
            except:
                try:
                    return self.montarUsuario(sessao.idprofessor.email)
                except:
                    return Usuario(404, None, None, None, None, None, None, None, None)
