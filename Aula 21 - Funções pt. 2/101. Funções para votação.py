def vote(birth_year):
    from datetime import date # isso economiza memória
    today_year = date.today().year
    age = today_year - birth_year
    if ((age >= 18) and (age < 70)) or ((age < 70) and (age >= 18)):
        s = f'Como você tem {age} anos, você vota.'
        return s
    elif age <= 15:
        s = f'Como você tem {age} anos, você não vota.'
        return s
    else:
        s = f'Como você tem {age} anos, seu voto é opcional.'
        return s


year = int(input('Em que ano você nasceu? '))
print(vote(year))
