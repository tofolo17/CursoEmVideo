from random import randint
from time import sleep
rnd = randint(0, 5)
print('-=-' * 21)
print('Vou pensar em um número que está entre 0 e 5. Tente advinhar...')
print('-=-' * 21)
chute_user = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
if chute_user == rnd:
    print('Boa arrombado')
else:
    print('kkkkkkkkk otário, tenta dnv ae cuzão')