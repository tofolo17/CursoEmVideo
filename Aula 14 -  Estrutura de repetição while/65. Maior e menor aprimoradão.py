resp = 'S'
s = i = 0
numbers = []
while resp == 'S':
    n = float(input('Digite um número: '))
    numbers.append(n)
    s += n
    i += 1
    resp = input('Deseja continuar? [S/N]').upper().strip()
print('Você digitou {} números e a média foi {}'.format(i, s/i))
print('O maior valor foi {} e o menor foi {}'.format(max(numbers), min(numbers)))
