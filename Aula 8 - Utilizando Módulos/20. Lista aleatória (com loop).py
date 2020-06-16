from random import shuffle
alunos = []
i = 0
while i < 4:
    aluno = str(input('Digite o nome do seu aluno: '))
    i = i+1
    alunos.append(aluno)
shuffle(alunos)
print(alunos)
