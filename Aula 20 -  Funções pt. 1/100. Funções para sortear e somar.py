from random import randint
from time import sleep
rnd_values = []


def sort():
    qtd = randint(1, 10)
    print(f'Sorteando valores da lista: ', end='')
    for x in range(0, qtd, 1):
        rnd_values.append(randint(1, 10))
    for x in range(len(rnd_values)):
        print(f'[{rnd_values[x]}]  ', end='')
        sleep(0.5)


def analysis():
    s = 0
    for x in rnd_values:
        if x % 2 == 0:
            s += x
    print(f'A soma dos valores pares dessa lista é: {s}.')


sort()
print()
analysis()
