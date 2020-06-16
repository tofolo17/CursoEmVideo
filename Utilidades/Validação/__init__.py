from Utilidades.Personalização import amarelo, error


def validaropcoes(qtd_options):
    while True:
        choice = input(f'{amarelo("Sua opção: ")}')
        try:
            int_c = int(choice)
            if int_c not in range(1, qtd_options + 1):
                print(error('Opção inválida.'))
            else:
                break
        except ValueError:
            print(error('Opção inválida.'))
    return int_c


def validarstr(txt):
    while True:
        var = input(f'{txt}').title().strip()
        if type(var) == str and var.isalpha():
            return var
        else:
            print(error('Valor inválido.'))


def validarint(txt):
    while True:
        try:
            var = int(input(f'{txt}'))
            return var
        except:
            print(error('Valor inválido.'))