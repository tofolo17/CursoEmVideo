qtd = int(input('Número de ativides: '))
alunos, dados = [], []
s = 0
while True:
    name = input('Nome: ').title().strip()
    dados.append(name)
    for x in range(qtd):
        at = int(input(f'{x + 1}° nota: '))
        s += at
        dados.append(at)
    dados.append(s/qtd)
    alunos.append(dados[:])
    dados.clear()
    s = 0
    resp = input('Deseja continuar? [S/N] ')
    if resp not in 'Ss':
        break
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
for x in range(len(alunos)):
    print(f'{x + 1:<4}{alunos[x][0]:<10}{alunos[x][-1]:>8.1f}')
while True:
    choice = int(input('Mostrar notas de qual aluno? [999 p/ parar] '))
    for x in range(len(alunos)):
        if choice == alunos.index(alunos[x]) + 1:
            print(f'O aluno {alunos[x][0]} tirou:', end='')
            for i in range(1, qtd + 1):
                print(f' [{alunos[x][i]}]', end='')
            print()
        else:
            continue
    if choice == 999:
        break
