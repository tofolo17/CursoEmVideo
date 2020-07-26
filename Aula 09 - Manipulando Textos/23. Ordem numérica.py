n = int(input('0 a 9999: '))
n_str = str(n)
pos = []
i = 0
while i < len(n_str):
    pos.append(n_str[i])
    i = i+1
if n < 10:
    print('Unidade: ', pos[0])
elif (n > 9) and (n < 100):
    print('Dezena: {}\nUnidade: {}'.format(pos[0], pos[1]))
elif (n > 99) and (n < 1000):
    print('Centena: {}\nDezena: {}\nUnidade: {}'.format(pos[0], pos[1], pos[2]))
else:
    print('Milhar: {}\nCentena: {}\nDezena: {}\nUnidade: {}'.format(pos[0], pos[1], pos[2], pos[3]))
