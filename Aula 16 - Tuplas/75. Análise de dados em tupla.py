qtd = int(input('Quantidade de valores: '))
n = tuple(int(input('Digite o {}º numero: '.format(i+1))) for i in range(qtd))
cont = 0
print(n)
print(n.count(9))
print(n.index(3) if n.count(3) > 0 else 0)
for i in range(0, qtd):
    if n[i] % 2 == 0:
        cont += 1
    else:
        continue
print(cont)
