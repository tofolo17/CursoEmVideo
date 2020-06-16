dados = dict()
galera = list()
total_age = 0
while True:
    dados['Nome'] = input('Nome: ').title().strip()
    while True:
        dados['Sexo'] = input('Sexo [M/F]: ').upper().strip()
        if dados['Sexo'] not in 'MF':
            print('Erro. Tente novamente.')
        else:
            break
    dados['Idade'] = int(input('Idade: '))
    total_age += dados['Idade']
    galera.append(dados.copy())
    dados.clear()
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp not in 'SN':
            print('Erro. Tente novamente.')
        else:
            break
    if resp == 'N':
        print(f'A) Ao todo temos {len(galera)} cadastrados.')
        print(f'B) A média de idade é de {total_age / len(galera)} anos.')
        print(f'C) As mulheres cadastradas são: ', end='')
        for d in galera:
            if d['Sexo'] == 'F':
                print(f'[{d["Nome"]}] ', end='')
        print()
        print(f'D) Pessoas acima da idade média: ')
        for d in galera:
            if d['Idade'] > total_age / len(galera):
                print(f'Nome: {d["Nome"]}; Sexo: {d["Sexo"]}; Idade: {d["Idade"]}')
        break
