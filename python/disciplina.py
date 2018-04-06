class Disciplina:

    def __init__(self, nome, cargaHoraria, mensalidade, professor):
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        self.__mensalidade= mensalidade
        self.__professor = professor

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def setCargaHoraria(self, novaCargaHoraria):
        self.__cargaHoraria = novaCargaHoraria

    def getMensalidade(self):
        return self.__mensalidade

    def setMensalidade(self, novoMensalidade):
        self.__mensalidade = novoMensalidade

    def getProfessor(self):
        return self.__professor

    def setProfessor(self, novoProfessor):
        self.__professor = novoProfessor

    def retornaValorHora(self):
        valor = self.mensalidade*6 / self.__cargaHoraria
        return valor

