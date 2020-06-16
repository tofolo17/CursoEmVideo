user_input = input("Digite algo: ")
try:
    val = int(user_input)
    print("O número digitado é do tipo int.")
except ValueError:
    try:
        val1 = float(user_input)
        print("O número digitado é do tipo float.")
    except ValueError:
        print("O que foi digitado é do tipo string.")

'''
A proposta inicial era verificar os 'is' do valor digitado. Mas me empolguei na
verificação dos tipos primitivos.

O tipo string pode guardar números, e esses podem ser verificados com o isnumeric.
'''