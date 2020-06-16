temp, princ = [], []
mai = men = 0
while True:
    temp.append(input('Nome: ').strip().title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if mai < temp[1]:
            mai = temp[1]
        if men > temp[1]:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = input('Deseja continuar? [S/N] ').strip()
    if resp in 'Nn':
        print(f'Registros: {len(princ)}.')
        print(f'O maior peso foi de {mai}kg. Dos seguintes: ', end='')
        for p in princ:
            if p[1] == mai:
                print(f'[{p[0]}] ', end='')
        print()
        print(f'O menor peso foi de {men}kg. Dos seguintes: ', end='')
        for p in princ:
            if p[1] == men:
                print(f'[{p[0]}] ', end='')
        break
