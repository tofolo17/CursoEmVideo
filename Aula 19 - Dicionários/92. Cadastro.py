from datetime import date
year = date.today().year
dados = dict()
dados['Nome'] = input('Nome: ').title().strip()
dados['Idade'] = year - int(input('Ano de nascimento: '))
dados['Carteira de Trabalho'] = int(input('Carteira de trabalho (0 se ná tiver): '))
if dados['Carteira de Trabalho'] != 0:
    dados['Ano de contratação'] = int(input('Ano de Contratação: '))
    dados['Salário R$'] = float(input('Salário: R$ '))
    dados['Idade quando aposentado'] = dados['Idade'] + 35
for k, v in dados.items():
    print(f'{k} {v}')
