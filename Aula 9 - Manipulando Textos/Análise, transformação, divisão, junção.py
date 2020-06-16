# Análise
frase = 'Por favor, ministro, aceite o Ramage'
print(len(frase))
print(frase.count('o'))
# print(frase.count('o', 0, 13)) --> Contagem com fatiamento
print(frase.find('age'))
print('Ramage' in frase)

# Transformação
frase1 = frase.replace('Ramage', 'Ramalho') # As string são imutáveis
print(frase1)
print(frase.upper())
print((frase.upper()).lower())
print(frase.capitalize()) # Só o primeiro em maiúsculo
print(frase.title()) # Capitalize palavra por palavra
print(frase.strip()) # Remove espaços inúteis
# frase.rstrip trata pela direita, e o lstrip, pela esquerda

# Divisão
dividido = frase.split()
print(dividido)
print(dividido[5])
print(dividido[5][1])
# Separa as palavras e transforma cada uma em uma cadeira distinta

# Junção
print('-'.join(frase.split()))
# Regera uma string única com um separador pré determinado

print("""
……………………„„-~^^~„-„„_
………………„-^*'' : : „'' : : : : *-„
…………..„-* : : :„„--/ : : : : : : : '\
…………./ : : „-* . .| : : : : : : : : '|
……….../ : „-* . . . | : : : : : : : : |
………...\„-* . . . . .| : : : : : : : :'|
……….../ . . . . . . '| : : : : : : : :|
……..../ . . . . . . . .'\ : : : : : : : |
……../ . . . . . . . . . .\ : : : : : : :|
……./ . . . . . . . . . . . '\ : : : : : /
….../ . . . . . . . . . . . . . *-„„„„-*'
….'/ . . . . . . . . . . . . . . '|
…/ . . . . . . . ./ . . . . . . .|
../ . . . . . . . .'/ . . . . . . .'|
./ . . . . . . . . / . . . . . . .'|
'/ . . . . . . . . . . . . . . . .'|
'| . . . . . \ . . . . . . . . . .|
'| . . . . . . \„_^- „ . . . . .'|
'| . . . . . . . . .'\ .\ ./ '/ . |
| .\ . . . . . . . . . \ .'' / . '|
| . . . . . . . . . . / .'/ . . .|
| . . . . . . .| . . / ./ ./ . .|

………………………………………._¸„„„„_
…………………….…………...„--~*'¯…….'\
………….…………………… („-~~--„¸_….,/ì'
…….…………………….¸„-^"¯ : : : : :¸-¯"¯/'
……………………¸„„-^"¯ : : : : : : : '\¸„„,-"
**¯¯¯'^^~-„„„----~^*'"¯ : : : : : : : : : :¸-"
.:.:.:.:.„-^" : : : : : : : : : : : : : : : : :„-"
:.:.:.:.:.:.:.:.:.:.: : : : : : : : : : ¸„-^¯
.::.:.:.:.:.:.:.:. : : : : : : : ¸„„-^¯
:.' : : '\ : : : : : : : ;¸„„-~"
:.:.:: :"-„""***/*'ì¸'¯
:.': : : : :"-„ : : :"\
.:.:.: : : : :" : : : : \,
:.: : : : : : : : : : : : 'Ì
: : : : : : :, : : : : : :/
"-„_::::_„-*__„„~"
""")
