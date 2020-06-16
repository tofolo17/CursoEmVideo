aluno = dict()
aluno['Nome'] = input('Nome: ').strip().title()
aluno['Média'] = float(input('Média: '))
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
else:
    aluno['Situação'] = 'Recuperação'
for k, v in aluno.items():
    print(f'{k} = {v}')
