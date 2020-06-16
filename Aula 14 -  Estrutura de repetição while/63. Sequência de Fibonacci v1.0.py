n = int(input('Escreva quantos números quer da Sequência de Fibonacci: '))
f = [0, 1]
for c in range(0, n):
    f.append(f[c] + f[c + 1])
print(f[:n])

# melhor resolução encontrada

'''
n = int(input('Digite o número de termos: '))
t1 = 0
t2 = 1
print('{} --> {} --> '.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print('{} --> '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
'''