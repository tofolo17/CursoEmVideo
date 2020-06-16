from time import sleep
from random import choice
resp = 's'
while resp.upper() == 'S':
    print('SUAS OPÇÕES:')
    print('[0] PEDRA')
    print('[1] PAPEL')
    print('[2] TESOURA')
    user_choice = int(input('Qual é a sua jogada? '))
    options = ['Pedra', 'Papel', 'Tesoura']
    if user_choice == 0:
        user_choice = options[0]
    elif user_choice == 1:
        user_choice = options[1]
    elif user_choice == 2:
        user_choice = options[2]
    else:
        while user_choice != 0 and user_choice != 1 and user_choice != 2:
            user_choice = int(input('Opção inválida. Qual é a sua jogada? '))
    cpu_choice = choice(options)
    sleep(0.25)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PO !!!')
    if cpu_choice == user_choice:
        print('Temos um empate! Nós escolhemos {}.'.format(cpu_choice))
    else:
        if cpu_choice == 'Pedra':
            if user_choice == 'Tesoura':
                print('Hahaha, jogou {} foi? Tome uma {}!'.format(user_choice, cpu_choice))
            else:
                print('Ih rapaz, {} ganha da minha {}.'.format(user_choice, cpu_choice))
        elif cpu_choice == 'Tesoura':
            if user_choice == 'Pedra':
                print('Tomei no boga. Sua {} arregaça minha {}.'.format(user_choice, cpu_choice))
            else:
                print('kkkkkkkk, vai ser cortado pela minha {} paizin.'.format(cpu_choice))
        else:
            if user_choice == 'Pedra':
                print('Toma essa embrulhada. Meu {} ganha da sua {}!'.format(cpu_choice, user_choice))
            else:
                print('Me fatiou hen mané. Meu {} não foi'
                      ' páreo para sua {}.'.format(cpu_choice, user_choice))
    resp = input('Deseja jogar novamente? (S/N) ')
    if resp.upper() == 'S':
        continue
    else:
        exit()