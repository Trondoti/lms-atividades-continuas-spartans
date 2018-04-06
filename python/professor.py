class Professor:

    def __init__(self, nome, email, ra, celular):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__disciplinas = []

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getEmail(self):
        return self.__email

    def setEmail(self, novoEmail):
        self.__email = novoEmail

    def getRa(self):
        return self.__ra

    def setRa(self, novoRa):
        self.__ra = novoRa

    def getCelular(self):
        return self.__celular

    def setCelular(self, novoCelular):
        self.__celular = novoCelular

    def getDisciplinas(self):
        return self.__disciplinas

    def adicionaDisciplina(self, disciplina):
        if self.getRa() != disciplina.getProfessor().getRa():
            return "RA Incompativel"
        self.__disciplinas.append(disciplina)

    def retornaSobrenome(self):
        return self.__nome.split(" ")[-1]

    def retornaCargaHoraria(self):
        cargaTotal = 0
        for disciplina in self.__disciplinas:
            cargaTotal += disciplina.getCargaHoraria()
        return cargaTotal / 4
