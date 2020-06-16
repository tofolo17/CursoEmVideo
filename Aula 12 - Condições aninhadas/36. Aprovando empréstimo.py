value_house = float(input('Qual o valor da casa? R$'))
value_salary = float(input('Quanto você ganha por mês? R$'))
years = int(input('O pagamento será feito em quantos anos? R$'))
pm = value_house / (years * 12)
if pm > 0.3 * value_salary:
    print('O valor da prestação mensal será de R${:.2f}, e como esse valor'
          ' é maior que 30% do seu salário, negamos o seu pedido.'.format(pm))
else:
    print('Parabéns. Pedido aprovado!!!')
