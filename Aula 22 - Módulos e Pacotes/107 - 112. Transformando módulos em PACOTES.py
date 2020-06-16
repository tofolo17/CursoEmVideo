from Utilidades.Dados import resumo
from Utilidades.Moeda import leiadinheiro

p = leiadinheiro('Digite o preço: ')
a = int(input('Digite a taxa de aumento [%]: '))
r = int(input('Digite a taxa de redução [%]: '))
resumo(p, a, r)
