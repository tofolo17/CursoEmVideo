s = 0
price_list, expensive = [], []
while True:
    name = input('Nome do produto: ').strip()
    price = float(input('Preço: R$ '))
    if price >= 1000:
        expensive.append('')
    resp = input('Deseja continuar? [S/N]').upper().strip()
    price_list.append(price)
    s += price
    if resp == 'S':
        continue
    else:
        break
print(s)
print(len(expensive))
print(min(price_list))
