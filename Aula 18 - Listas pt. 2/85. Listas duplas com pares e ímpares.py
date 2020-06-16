qtd = int(input('Quantidade de valores: '))
num = [[], []]
for x in range(qtd):
    n = int(input(f'Digite o {x+1}° número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
print(f'Os números pares são: {num[0]}')
num[1].sort()
print(f'Os números ímpares são: {num[1]}')