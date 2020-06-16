def save(qtd, sit=0):
    saved = list()
    data = dict()
    s = 0
    for x in range(1, qtd + 1, 1):
        n = int(input(f'Valor da {x}° nota: '))
        saved.append(n)
        s += n
    data['Total'] = qtd
    data['Maior'] = max(saved)
    data['Menor'] = min(saved)
    data['Média'] = s/qtd
    if data['Média'] > 7:
        situation = 'Ótimo'
    elif data['Média'] < 5:
        situation = 'Péssimo'
    else:
        situation = 'Mediano'
    if sit:
        data['Situação'] = situation
    return data


print(save(int(input('Insira o número de atividades: ')), sit=True))
