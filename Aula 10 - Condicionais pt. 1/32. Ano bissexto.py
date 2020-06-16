from datetime import date

a = int(input(''))

if a == 0:
    a = date.today().year

if a % 4 == 0:
    print('bissexto')
else:
    print('normal')
