import time
from classes import *
lider = False

print('bem vindo ao sistema do JICS')
escolhaInicial = input('Você é professor ou aluno? se for professor, digite 1. Se for aluno, digite 2.')
if escolhaInicial == '1':
    print('Qual o seu nome completo?')
    nomeProfessor = input()
    print('Qual o seu número de matrícula?')
    matriculaProfessor = input()
    print('Qual o seu curso?')
    cursoProfessor = input()
    
    cadastroProfessor = Professor(matriculaProfessor, nomeProfessor, cursoProfessor)
    cadastroProfessor.verInformacoesProfessor()

elif escolhaInicial == '2':
    print('Você é líder da sua turma? Se sim, digite 1. Se não, digite 2.')
    lideranca = input()
    if lideranca  == '1':
        print('Qual o seu nome completo?')
        nomeLider = input()
        print('Qual o seu número de matrícula?')
        matriculaLider = input()
        print('Qual a sua data de nascimento?')
        dataLider = input()
        print('Qual o seu curso?')
        cursoLider = input()
        print('Qual a sua turma?')
        turmaLider = input()

        cadastroLider = Lider(matriculaLider, nomeLider, cursoLider, turmaLider)
        cadastroLider.verInformacoesLider()





    elif lideranca == '2':
        print('Qual o seu nome completo?')
        nomeAluno = input()
        print('Qual o seu número de matrícula?')
        matriculaAluno = input()
        print('Qual a sua data de nascimento?')
        dataAluno = input()
        print('Qual o seu curso?')
        cursoAluno = input()
        print('Qual a sua turma?')
        turmaAluno = input()

        cadastroAluno = Aluno(matriculaAluno, nomeAluno, cursoAluno, turmaAluno)
        cadastroAluno.verInformacoesAluno()

