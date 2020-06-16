a = int(input('Digite o primeiro termo da PA: '))
b = int(input('Digite a razão da PA: '))
c = int(input('Digite a quantidade de termos da PA: '))
d = 0
i = 0
lt = a + (c-1) * b
while d < lt:
    i = i + 1
    d = d + b
    print('{} --> '.format(d), end='')
print('PAUSA')
x = 1
while x != 0:
    x = int(input('Quantos termos você quer mostrar a mais? '))
    rlt = a + (c+x-1) * b
    while lt + 1 < rlt:
        lt += b
        print('{} --> '.format(lt), end='')
    c += x
    if x != 0:
        print('PAUSA')
print('Progressão finalizada.')