def leiaint(integer):
    while True:
        valid = input(integer)
        if not valid.isnumeric():
            print('Erro. Tente novamente.')
        else:
            break
    return valid


n = leiaint('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}.')