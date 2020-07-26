from math import sin, cos, radians
rad = float(input('Digite o valor de um ângulo (em graus): '))
ang = radians(rad)
print('{:.3f} \n{:.3f}'.format(sin(ang), cos(ang)))

# Sim, eu poderia ter feito isso com a tangente.
