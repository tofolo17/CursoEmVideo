from unidecode import unidecode
phrase = input('Digite uma frase: ')
direct = unidecode(phrase).upper()
inverse = direct[::-1]
if direct.replace(' ', '') == inverse.replace(' ', ''):
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo')
