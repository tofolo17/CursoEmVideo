from random import randint
qtd = int(input('Quantidade de jogos: '))
mega = [[] for jogo in range(qtd)]
for i in range(0, qtd):
    for j in range(0, 6):
        n = randint(1, 60)
        if n not in mega[i]:
            mega[i].append(n)
        else:
            while True:
                n = randint(1, 60)
                mega[i].append(n)
                if n in mega:
                    mega[i].remove(n)
                else:
                    break
for i in range(0, qtd):
    print(sorted(mega[i]))
