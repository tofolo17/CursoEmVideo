value = float(input('Qual o valor a ser pago? R$'))
print('FORMAS DE PAGAMENTO')
print('[1] À vista dinheiro/cheque')
print('[2] À vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
option = int(input('Qual é a opção? '))
if option == 1:
    value_to_pay = value - (value * 10/100)
    print('O pagamento será de: R${}'.format(value_to_pay))
elif option == 2:
    value_to_pay = value - (value * 5 / 100)
    print('O pagamento será de: R${}'.format(value_to_pay))
elif option == 3:
    value_to_pay = value / 2
    print('Cada parcela tem um valor de: R${}'.format(value_to_pay))
elif option == 4:
    n_portion = int(input('Quantas parcelas? '))
    if n_portion < 3:
        while n_portion < 3:
            print('Esse valor é inválido. Tente novamente')
            n_portion = int(input('Quantas parcelas? '))
    value_to_pay = (value + (value * 20/100)) / n_portion
    print('Cada parcela ({} no total) tem um valor de: R${}'.format(n_portion, value_to_pay))
else:
    print('Ajuda nóis né arrombado.')