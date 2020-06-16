qtd = int(input('Quantos valores? '))
number = []
i = 1
s = 0
m = 1
resp = 0
while resp !=5:
    while i < qtd + 1:
        n = float(input('Digite o {}° valor: '.format(i)))
        number.append(n)
        i = i + 1
        s = s + n
        m = m * n
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos números')
    print('[5] Sair')
    resp = int(input('>>>>> Qual a sua opção? '))
    if resp == 1:
        print('Resultado: {:.1f}'.format(s))
    elif resp == 2:
        print('Resultado: {:.1f}'.format(m))
    elif resp == 3:
        print('Resultado: {}'.format(max(number)))
    elif resp == 4:
        i = 1
        s = 0
        m = 1
        number = []
        qtd = int(input('Quantos valores? '))
print('FIM')
exit()