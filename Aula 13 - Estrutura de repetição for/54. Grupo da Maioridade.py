from datetime import date
qtd = int(input('Quantas pessoas deseja analisar? '))
i = 1
people = []
adult = []
kid = []
while i < qtd + 1:
    day = int(input('Dia: '))
    month = int(input('Mês: '))
    year = int(input('Ano: '))
    print('-=-' * 6)
    date_btd = date(year, month, day)
    date_now = date.today()
    age = (date_now - date_btd) / 365.25
    int_age = int(age.days)
    people.append(int_age)
    i = i + 1
for x in range(0, len(people), 1):
    if people[x] >= 18:
        adult.append(x)
    else:
        kid.append(x)
print('Nessa lista temos: {} de maior e {} de menor.'.format(len(adult), len(kid)))
