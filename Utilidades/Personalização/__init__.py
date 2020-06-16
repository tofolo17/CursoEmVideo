def mostralinha():
    print('-' * 30)


def amarelo(a):
    return f'\033[33m{a}\033[m'


def azul(a, bold=0):
    if bold:
        return f'\033[1:34m{a}\033[m'
    else:
        return f'\033[34m{a}\033[m'


def error(a):
    return f'\033[31m{a.upper()}\033[m'


def titulo(a, alcance):
    print('-' * alcance)
    print(f'{a}'.center(alcance))
    print('-' * alcance)