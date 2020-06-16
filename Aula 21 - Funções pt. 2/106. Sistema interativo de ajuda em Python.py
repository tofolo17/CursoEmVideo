def helper(command):
    if command == 'fim':
        print('Volte sempre.')
    else:
        help(command)


while True:
    doubt = input('Função ou biblioteca: ').upper().lower()
    helper(doubt)
    if doubt == 'fim':
        break
