import math
alt = float(input('Digite a altura da parede a ser pintada (em metros): '))
larg = float(input('Agora, a largura dela: '))
plt = float(input('Qual o preço do litro da tinta? R$ '))
mlt = float(input('Quantos m² um litro de tinta pinta? '))
area = alt * larg
qtdlitros = math.ceil(area / mlt)
preco = qtdlitros * plt
print('Sua parede tem uma área de {:.2f} m². Você precisará de {:.2f}'
      ' litros para pintá-la, e isso equivale a R$ {:.2f}'.format(area, qtdlitros, preco))
