def leiaint(a):
    while True:
        try:
            user_n = int(a)
            return print('O número é inteiro.')
        except ValueError:
            try:
                user_n = float(a)
                return print('O número é real.')
            except ValueError:
                print('ERRO: Tente novamente.')
                a = input('Digite um valor: ')


leiaint(input('Digite um valor: '))
