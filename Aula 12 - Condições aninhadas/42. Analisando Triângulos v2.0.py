i = 1
sides = []
while i < 4:
    side = float(input('Digite o valor do {}° lado: '.format(i)))
    sides.append(side)
    i = i + 1
if int(sides[0]) == int(sides[1]) == int(sides[2]):
    print('O triângulo é equilátero.')
elif int(sides[0]) != int(sides[1]) != int(sides[2]):
    print('O triângulo é escaleno.')
else:
    print('O triângulo é isósceles.')
