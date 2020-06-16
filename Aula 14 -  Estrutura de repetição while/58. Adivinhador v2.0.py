from random import randint
rnd = randint(0, 10)
print('-=-' * 21)
print('Vou pensar em um número que está entre 0 e 10. Tente advinhar...')
print('-=-' * 21)
resp = 0
i = 0
while resp == 0:
    chute_user = int(input('Em que número eu pensei? '))
    i = i + 1
    if chute_user == rnd:
        print('Bom, você precisou de {} tentativa(s) para acertar.'.format(i))
        resp = 1
    else:
        print('Tente novamente! ')
        continue
