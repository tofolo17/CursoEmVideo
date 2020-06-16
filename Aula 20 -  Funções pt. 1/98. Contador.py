from time import sleep
def contador(inicio, fim, passo):
    if fim > inicio:
        fim = fim + 1
    else:
        fim = fim - 1
    for x in range(inicio, fim, passo):
        print(f'[{x}] ', end='')
    sleep(1)
    print()


contador(1, 10, 1)
contador(0, 10, 2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
