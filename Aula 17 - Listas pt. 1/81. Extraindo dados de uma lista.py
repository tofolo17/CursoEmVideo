lis = []
while True:
    lis.append(int(input('Digite um número: ')))
    resp = input('Deseja continuar? [S/N] ').lower()
    if resp != 's':
        lis.sort(reverse=True)
        print(f'Você digitou {len(lis)} valores.')
        print(f'Em ordem decrescente: {lis}')
        print('O 5 está na lista.' if 5 in lis else 'O 5 não está na lista')
