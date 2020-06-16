linhas = int(input('Quantas linhas? '))
colunas = int(input('Quantas colunas? '))
matriz = [[] for linha in range(linhas)]
par = s = mai = 0
for i in range(0, linhas):
    for j in range(0, colunas):
        n = int(input(f'Digite o valor [{i + 1},{j + 1}]: '))
        matriz[i].append(n)
        if n % 2 == 0:
            par += n
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
for i in range(0, linhas):
    s += matriz[i][0]
for i in range(0, colunas):
    if i == 0:
        matriz[0][i] = mai
    else:
        if matriz[0][i] > mai:
            mai = matriz[0][i]
print(f'A soma dos valores pares vale: {par}.')
print(f'A soma dos valores da primeira coluna é: {s}')
print(f'O maior valor da 1° linha é: {mai}')
