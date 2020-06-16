number = []
while True:
    n = int(input('Digite um valor: '))
    if n not in number:
        number.append(n)
        resp = (input('Valor adicionado. Inserir outro? [S/N] ')).lower()
        if resp != 's':
            break
    else:
        print('Valor já adicionado. Tente novamente.')
print(f'Você digitou os valores {number}.')