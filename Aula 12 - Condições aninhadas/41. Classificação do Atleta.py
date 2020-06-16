from datetime import date
print('Informe sua data de nascimento: ')
day = int(input('Dia: '))
month = int(input('Mês: '))
year = int(input('Ano: '))
date_btd = date(year, month, day)
date_now = date.today()
age = (date_now - date_btd)/365.25
int_age = int(age.days)
if int_age <= 9:
    print('Você tem {} anos, e é um atleta MIRIM.'.format(int_age))
elif int_age <= 14:
    print('Você tem {} anos, e é um atleta INFANTIL.'.format(int_age))
elif int_age <= 19:
    print('Você tem {} anos, e é um atleta JUNIOR.'.format(int_age))
elif int_age <= 25:
    print('Você tem {} anos, e é um atleta SÊNIOR.'.format(int_age))
else:
    print('Você tem {} anos, e é um atleta MASTER.'.format(int_age))