n = int(input("Digite um número inteiro e veja sua tabuada: "))
m1 = int(input("Valor inicial da multiplicação: "))
m2 = int(input("Valor final da multiplicação: "))
i = 0
resp = 'S'
print('=' * 12)
while resp == 'S':
    while (m1 + i) <= m2:
        f = m1 + i
        r = n * f
        i = i + 1
        print('{} x {:2} = {}'.format(n, f, r))
    print('=' * 12)
    resp = input('Deseja inserir outros valores? [S/N] ').upper()
    if resp == 'S':
        n = int(input("Digite um número inteiro e veja sua tabuada: "))
        m1 = int(input("Valor inicial da multiplicação: "))
        m2 = int(input("Valor final da multiplicação: "))
        i = 0
    else:
        break