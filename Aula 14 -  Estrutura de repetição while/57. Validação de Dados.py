sex = input('Informe seu sexo [M/F]: ').strip().upper()
while sex not in 'MF':
    sex = input('Valor inválido. Informe seu sexo [M/F]: ').strip().upper()
print('Sexo registrado ({}).'.format(sex))

'''
p = 0
while p == 0:
    sex = input('Sexo [M/F]: ')
    mf = sex.upper()
    if mf == 'M':
        print('Você é um macho.')
        exit()
    elif mf == 'F':
        print('Você é uma fêmea.')
        exit()
    else:
        print('Tente novamente.')
        continue
'''