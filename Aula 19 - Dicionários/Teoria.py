estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')

'''
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['uf'])
'''

'''
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 18}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

# del pessoas['sexo']
# pessoas['nome'] = 'Leandro'
# pessoas['Peso'] = 98.5
