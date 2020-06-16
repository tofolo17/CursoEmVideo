qtd = int(input('Você deseja comparar quantas pessoas? '))
i = 1
girl_age, men_age, men_name = [], [], []
sum_i = 0
while i < qtd + 1:
    print('----- {}° PESSOA -----'.format(i))
    name = input('Nome: ')
    age = int(input('Idade: '))
    sx = input('Sexo [M/F]: ')
    sex = sx.upper()
    if (sex == 'F') and (age <= 20):
        girl_age.append('')
    if sex == 'M':
        men_name.append(name)
        men_age.append(age)
    sum_i = sum_i + age
    i = i + 1
med = sum_i / qtd
older_own = men_name[men_age.index(max(men_age))]
print('A idade média é de {:.1f}.'.format(med))
print('O homem mais velho tem {} anos e se chama {}.'.format(max(men_age), older_own))
print('Ao todo temos {} mulher(es) com menos de 20 anos.'.format(len(girl_age)))