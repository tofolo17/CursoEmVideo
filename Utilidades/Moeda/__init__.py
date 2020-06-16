def leiadinheiro(texto):
    while True:
        valor = str(input(texto)).strip().replace(',', '.')
        if valor.replace('.', '').isnumeric():
            break
        print(f'\033[1;31mO valor digitado \"{valor}\", é um preço inválido!\033[m')
    return float(valor)
