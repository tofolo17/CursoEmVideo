from math import factorial
n = int(input('Digite um número: '))
print('O fatorial de {} vale: '.format(n), end='')
for x in range(n, 1, -1):
    print(x, 'x ', end='')
print('1 ', end='')
print('=', factorial(n))

'''
n = int(input('Digite um número: '))
c = n
f = 1
while c > 0:
    print('{}.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f = f * c
    c -= 1
print(f)
'''