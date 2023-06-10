import time
from cores import *

class ParticipanteJics:
    def __init__(self, matricula, nome, curso):
        self.matricula = matricula
        self.nome = nome
        self.curso = curso

class Professor (ParticipanteJics):
    def __init__(self, matricula, nome, curso):
        super().__init__(matricula, nome, curso)
    
    def verInformacoesProfessor (self):
        print('BOLETIM DE CADASTRO: ')
        print('NOME: ', self.nome)
        print('CURSO: ', self.curso)
        print('MATRÍCULA: ', self.matricula)

class Aluno (ParticipanteJics):
    def __init__(self, matricula, nome, curso, turma):
        super().__init__(matricula, nome, curso)
        self.turma = turma

    def verInformacoesAluno (self):
        print('BOLETIM DE CADASTRO: ')
        print('NOME:', self.nome)
        print('MATRÍCULA: ', self.matricula)
        print('CURSO: ', self.curso)
        print('TURMA: ', self.turma)
        print('LIDERANÇA? NÃO')

class Lider (Aluno):
    def __init__(self, matricula, nome, curso, turma):
        super().__init__(matricula, nome, curso, turma)
    
    def verInformacoesLider (self):
        print('BOLETIM DE CADATRO: ')
        print('NOME: ', self.nome)
        print('MATRÍCULA: ', self.matricula)
        print('CURSO: ', self.curso)
        print('TURMA: ', self.turma)
        print('LIDERANÇA? SIM')
    
