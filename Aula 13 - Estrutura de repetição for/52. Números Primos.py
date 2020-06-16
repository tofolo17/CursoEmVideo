n = int(input('Digite um número: '))
divisions = []
for x in range(1, n + 1, 1):
    if n % x == 0:
        divisions.append(n)
    else:
        continue
if len(divisions) <= 2:
    print('O número {} é primo.'.format(n))
else:
    print('Como esse número é divisível por outros {} números, ele não é primo.'
          ''.format(len(divisions)))
