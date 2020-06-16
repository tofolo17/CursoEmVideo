lis, par, imp = [], [], []
while True:
    n = int(input('Digite um número: '))
    lis.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        imp.append(n)
    resp = input('Deseja continuar? [S/N] ').lower().strip()
    if resp != 's':
        print(f'Lista completa: {lis}')
        print(f'Lista de pares: {par}')
        print(f'Lista de ímpares: {imp}')
        break
