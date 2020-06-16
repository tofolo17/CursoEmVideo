qtd = int(input('Você digitará quantos números? '))
numbers = []
i = 0
s = 0
while i < qtd:
    n = int(input('Digite um número: '))
    numbers.append(n)
    i = i + 1
for x in range(len(numbers)):
    if numbers[x] % 2 == 0:
        s = s + int(numbers[x])
    else:
        continue
if s == 0:
    print('Você não digitou nenhum número par.')
else:
    print('A soma dos números pares vale {}.'.format(s))
