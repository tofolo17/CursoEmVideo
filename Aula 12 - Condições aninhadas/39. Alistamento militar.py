from datetime import date
print('Informe sua data de nascimento: ')
day = int(input('Dia: '))
month = int(input('Mês: '))
year = int(input('Ano: '))
date_btd = date(year, month, day)
date_now = date.today()
age = (date_now - date_btd)/365.25
int_age = int(age.days)
if int_age < 18:
    years_to = 18 - int_age
    enlistment_year_to = date.today().year + years_to
    print('Você só se apresentará em {}.'.format(enlistment_year_to))
elif int_age > 18:
    years_ago = int_age - 18
    enlistment_year_ago = date.today().year + years_ago
    print('Você deveria ter se apresentado em {}.'.format(enlistment_year_ago))
elif (int_age == 18) and (date.today().year - year == int_age):
    print('Como você fez aniversário nesse ano, você se apresentará no ano que vem.')
elif (int_age == 18) and (date.today().year - year == int_age + 1) and date.today().month > 2:
    print('Você deveria ter se apresentado no começo do ano.')
else:
    print('Aliste-se IMEDIATAMENTE!')

'''
válido ao considerar experiência individual
(porém não sei quais as regras formais para 
o alistamento e a apresentação
'''
