from math import hypot
co = float(input('Digite o comprimento do primeiro cateto: '))
ca = float(input('Agora, o do segundo: '))
hip = hypot(ca, co)
# hip = sqrt(pow(ca, 2)+pow(co, 2))
print('{:.2f}'.format(hip))
