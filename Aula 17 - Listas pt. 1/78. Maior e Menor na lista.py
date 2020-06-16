qtd = int(input('Quantos valores deseja digitar? '))
i = 1
ns = []
for x in range(qtd):
    ns.append(int(input('Digite o {}° número: '.format(i))))
    i += 1
print(f'Valores digitados: {ns}')
print(f'Menor valor: {min(ns)}. Ele apareceu nas posições: ')
for pos, val in enumerate(ns):
    if val == min(ns):
        print(f'{pos}...', end='')
print('FIM')
print(f'Maior valor: {max(ns)}. Ele apareceu nas posições: ')
for pos, val in enumerate(ns):
    if val == max(ns):
        print(f'{pos}...', end='')
print('FIM')
