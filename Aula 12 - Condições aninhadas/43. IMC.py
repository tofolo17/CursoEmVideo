alt = float(input('Qual sua altura ? (m) '))
weight = float(input('Qual a sua massa? (kg) '))
imc = weight / (alt * alt)
if imc <= 18.5:
    ideal_weight = 18.51 * (alt * alt)
    fatten = ideal_weight - weight
    print('Seu IMC é {:.1f}. Você está abaixo do peso e precisa engordar'
          ' {:.1f} kg'.format(imc, fatten))
elif imc <= 25:
    print('Seu IMC é {:.1f}. Seu peso atual é o ideal.'.format(imc))
elif imc <= 30:
    ideal_weight = 25 * (alt * alt)
    lose_weight = weight - ideal_weight
    print('Seu IMC é {:.1f}. Você está acima do peso (sobrepeso) e precisa emagrecer'
          ' {:.1f} kg'.format(imc, lose_weight))
elif imc <= 40:
    ideal_weight = 25 * (alt * alt)
    lose_weight = weight - ideal_weight
    print('Seu IMC é {:.1f}. Você está acima do peso (obesidade) e precisa emagrecer'
          ' {:.1f} kg'.format(imc, lose_weight))
else:
    ideal_weight = 25 * (alt * alt)
    lose_weight = weight - ideal_weight
    print('Seu IMC é {:.1f}. Você está acima do peso (obesidade mórbida) e precisa emagrecer'
          ' {:.1f} kg'.format(imc, lose_weight))