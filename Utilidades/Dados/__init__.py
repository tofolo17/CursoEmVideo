def dobro(a):
    return a ** 2


def metade(a):
    return a/2


def triplo(a):
    return a ** 3


def aumento10(a):
    return a * 1.1


def moeda(a):
    return str(f'R${a:.2f}').replace('.', ',')


def resumo(preco, aumento, reducao):
    print(f'''
Preço analisado: {moeda(preco)}
Dobro do preço: {moeda(dobro(preco))}
Metade do preço: {moeda(metade(preco))}
Aumento de {aumento}%: {moeda(preco * (1 + aumento/100))}
Redução de {reducao}%: {moeda(preco * (1 - reducao/100))}
    ''')
