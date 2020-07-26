phrase = input('Digite uma frase: ').strip()

qtd_a = int(phrase.count('a'))
qtd_A = int(phrase.count('A'))
s = qtd_A + qtd_a
print(s)

# Tudo poderia ser facilitado jogando a frase inteira pra Upper

pos_A = int(phrase.find('A'))
pos_a = int(phrase.find('a'))
if (pos_A < pos_a) and (pos_A != -1):
    print(pos_A + 1)
else:
    print(pos_a + 1)

ult_A = int(phrase.rfind('A'))
ult_a = int(phrase.rfind('a'))
if (ult_A < ult_a) and (ult_A != -1):
    print(ult_A + 1)
else:
    print(ult_a + 1)
