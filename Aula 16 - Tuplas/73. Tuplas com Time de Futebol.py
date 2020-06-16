brasileirão = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
               'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
               'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
               'América-MG', 'Chapecoense', 'Vitória', 'Paraná')
print('\n{:=^35}'.format(' BRASILEIRÃO 2018 '))
print('''\nEscolha uma das opções abaixo para exibir:
[ A ] Os 5 primeiros
[ B ] Os últimos 4 colocados
[ C ] Times em ordem alfabética
[ D ] Em que posição está o seu time
[ E ] Sair''')
while True:
    opcao = str(input('Digite a opção desejada: ')).upper().strip()
    if opcao == 'A':
        for c in (brasileirão[0:5]):
            print(c)
    elif opcao == 'B':
        print(brasileirão[-4:])
    elif opcao == 'C':
        print(sorted(brasileirão))
    elif opcao == 'D':
        time = input('Nome do time: ').title()
        while time not in brasileirão:
            if time not in brasileirão:
                time = input('Erro. Tente novameente: ').title()
        print('O {} entá em {}°.'.format(time, brasileirão.index(time) + 1))
    elif opcao == 'E':
        break
