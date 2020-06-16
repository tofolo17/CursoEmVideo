linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))
matriz = [[] for linha in range(linhas)]
for i in range(0, linhas):
    for j in range(0, colunas):
        n = int(input(f'Digite o valor [{i + 1},{j + 1}]: '))
        matriz[i].append(n)
for i in range(0, linhas):
    for j in range(0, colunas):
        if colunas == 1:
            print(f'| {matriz[i][j]:^3} |', end='')
        else:
            if j == 0:
                print(f'| {matriz[i][j]:^3} ', end='')
            elif j == colunas - 1:
                print(f' {matriz[i][j]:^3} |', end='')
            else:
                print(f' {matriz[i][j]:^3} ', end='')
    print()
