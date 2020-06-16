from random import randint
cont = 1
prov = dict()
pos = list()
qtd = int(input('Quantidade de jogadores: '))
for c in range(0, qtd):
    prov[f'Jogador {c + 1}'] = randint(1, 6)
for k, v in prov.items():
    print(f'{k}: {v}')
print('RANKING')
for item in sorted(prov, key=prov.get, reverse=True):
    if prov[item] not in pos or item == 0:
        print(f'{cont}° lugar: {item.lower()} com {prov[item]}')
        pos.append(prov[item])
        cont += 1
    else:
        print(f'{cont-1}° lugar: {item.lower()} com {prov[item]}')

'''
ranking = sorted(jogo.items(), key=itemgetter(1), reverse = True) --> ordem de valor
vira uma lista
'''