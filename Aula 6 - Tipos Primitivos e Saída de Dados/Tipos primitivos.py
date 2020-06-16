n1 = int(input("Digite um número inteiro: "))
n2 = float(input("Digite um número real: "))
# Adiciona um ponto flutuante ao número, transformando-o em número real
print("O primeiro número é maior que o segundo?")
n3 = bool(n1 > n2)
if n3 == 'True':
    msg1 = str("Sim, é maior!")
    print(msg1)
else:
    msg2 = str("Não, é menor.")
    print(msg2)