numeros = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')
opt = int(input('Digite um número entre 0 e 20: '))
while True:
    if -1 < opt < len(numeros):
        print(numeros[opt])
        break
    else:
        opt = int(input('Erro. Tente novamente: '))