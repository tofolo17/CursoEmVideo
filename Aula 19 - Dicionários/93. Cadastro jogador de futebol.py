dados = dict()
lis = list()
s = 0
dados['Nome'] = input('Qual o nome do jogador? ').title().strip()
qtd = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(qtd):
    gols = int(input(f'    Quantos gols na {c+1}° partida? '))
    lis.append(gols)
    s += gols
dados['Gols'] = lis
dados['Total'] = s
print('-=-' * 13)
print(dados)
print('-=-' * 13)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-=-' * 13)
print(f'O jogador {dados["Nome"]} jogou {qtd} partidas.')
for x in range(len(lis)):
    print(f'    Na {x+1}° partida fez {lis[x]} gol(s).')
print(f'Foi um total de {s} gols.')
