exp = input('Digite a expressão: ')
pilha = []
for pos in range(exp):
    if pos == '(':
        pilha.append('(')
    elif pos == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Válido.')
else:
    print('Ínválido.')