def valid(nome=0, gols=0):
    if nome == '':
        nome = '<desconhecido>'
    if not gols.isnumeric():
        gols = '0'
    return f'O jogador {nome} fez {gols} gols.'


name = input('Qual o nome do jogador? ').title().strip()
g = input(f'Quantos gols {name} fez? ')
print(valid(name, g))
