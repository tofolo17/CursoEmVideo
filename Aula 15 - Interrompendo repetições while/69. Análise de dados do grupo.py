i = sum_i = 0
girl_age, men_age, men_name = [], [], []
while True:
    print('----- {}° PESSOA -----'.format(i + 1))
    name = input('Nome: ')
    age = int(input('Idade: '))
    sex = input('Sexo [M/F]: ').upper()
    if (sex == 'F') and (age <= 20):
        girl_age.append('')
    if sex == 'M':
        men_name.append(name)
        men_age.append(age)
    sum_i += age
    i += 1
    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'S':
        continue
    else:
        break
med = sum_i / i
older_own = men_name[men_age.index(max(men_age))]
print('A idade média é de {:.1f}.'.format(med))
print('O homem mais velho tem {} anos e se chama {}.'.format(max(men_age), older_own))
print('Ao todo temos {} mulher(es) com menos de 20 anos.'.format(len(girl_age)))