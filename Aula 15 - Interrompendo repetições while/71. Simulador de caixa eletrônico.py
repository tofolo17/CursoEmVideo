valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced_value = 50
ced_qtd = 0
while True:
    if total >= ced_value:
        total -= ced_value
        ced_qtd += 1
    else:
        if ced_qtd >= 0:
            print(f'Total de {ced_qtd} de R${ced_value}')
        if ced_value == 50:
            ced_value = 20
        elif ced_value == 20:
            ced_value = 10
        elif ced_value == 10:
            ced_value = 1
        ced_qtd = 0
        if total == 0:
            break
