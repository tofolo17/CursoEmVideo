def escreva(msg):
    align = int(len(msg) + 4)
    print('~' * align)
    print(f'  {msg}')
    print('~' * align)


mensagem = input('Digita alguma frase: ')
escreva(mensagem)
