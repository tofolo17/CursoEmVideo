dados = dict()
gols_p, team = list(), list()
cont = 1
s = 0
res = None
while True:
    while True:
        dados['Código'] = cont
        dados['Nome'] = input('Qual o nome do jogador? ').title().strip()
        qtd = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
        for c in range(qtd):
            gols = int(input(f'    Quantos gols na {dados["Código"]}° partida? '))
            gols_p.append(gols)
            s += gols
        dados['Gols'] = gols_p[:]
        dados['Total'] = s
        team.append(dados.copy())
        gols_p.clear()
        dados.clear()
        cont += 1
        s = 0
        while True:
            resp = input('Deseja cotinnuar? [S/N] ').upper()
            if resp not in 'SN':
                print('Erro. Tente novamente.')
            else:
                break
        if resp != 'N':
            continue
        else:
            break
    print('-=-' * 20)
    print(f'{"Código":<8}{"Nome":<15}{"Gols":<20}{"Total":<4}')
    for d in team:
        print(f'{d["Código"]:<8}{d["Nome"]:<15}{str(d["Gols"]):<20}{d["Total"]}')
    while True:
        player = int(input('Mostrar dados de qual jogador? [999 para parar] '))
        if (player == 0) or (player not in range(1, cont, 1)) and player != 999:
            print('Erro. Tente novamente.')
        elif player == 999:
            exit()
        else:
            for d in team:
                if d['Código'] == player:
                    res = d
            print("Informações sobre o jogador : " + str(res))
