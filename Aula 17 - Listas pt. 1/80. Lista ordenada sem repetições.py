qtd = int(input('Deseja inserir quantos valores? '))
lis = []
for x in range(qtd):
    n = int(input('Digite o {}° valor: '.format(x+1)))
    if x == 0 or n > lis[-1]:
        lis.append(n)
    else:
        pos = 0
        while pos < len(lis):
            if n <= lis[pos]:
                lis.append(pos, n)
                break
            pos += 1
print(lis)