ni = int(input('O número inicial é: '))
nf = int(input('O número final é: '))
s = 0
for x in range(ni, nf + 1, 1):
    if (x % 2 != 0) and (x % 3 == 0):
        print(x, '', end='')
        s = s + x
    else:
        continue
print('\n{}'.format(s))
