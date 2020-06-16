qtd = int(input('Quantidade de termos: '))
r = int(input('Razão: '))
first_term = int(input('Primeiro termo: '))
last_term = first_term + (qtd - 1) * r
for x in range(first_term, last_term, r):
    print(x, end=' --> ')
print(last_term)

# funciona muito bem para valores inteiros