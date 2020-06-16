ni = int(input('O número inicial é: '))
nf = int(input('O número final é: '))
if ni % 2 != 0:
    npi = ni + 1
    for x in range(npi, nf + 1, 2):
        print(x, '', end='')
else:
    for x in range(ni, nf + 1, 2):
        print(x, '', end='')

