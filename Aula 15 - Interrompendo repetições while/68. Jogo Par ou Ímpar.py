from random import randint, choice
i = 0
while True:
    cpu_choice = randint(1, 10)
    user_choice = int(input('Digite um valor de 1 a 10: '))
    value = cpu_choice + user_choice
    resp = ' '
    while resp not in 'PI':
        resp = input('Par ou Ímpar? [P/I] ').upper().strip()
    i += 1
    if resp == 'P':
        if value % 2 == 0:
            print(f'Eu escolhi {cpu_choice} e você {user_choice}, logo, '
                  f'você venceu.')
        else:
            print(f'Eu escolhi {cpu_choice} e você {user_choice}, logo, '
                  f'você perdeu na {i}° tentativa.')
            break
    elif resp == 'I':
        if value % 2 == 1:
            print(f'Eu escolhi {cpu_choice} e você {user_choice}, logo, '
                  f'você venceu.')
        else:
            print(f'Eu escolhi {cpu_choice} e você {user_choice}, logo, '
                  f'você perdeu na {i}° tentativa.')
            break
    print('-=-' * 4)
    print(f' {i + 1}°RODADA: ')
    print('-=-' * 4)