n1 = float(input("1° - "))
n2 = float(input("2° - "))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
div = n1 / n2
exp = n1 ** n2
# pow(n1, n2)
# n1 ** (1/2) = raiz quadrada de n1
# 'Oi' * 5 = OiOiOiOiOi
divEx = n1 // n2
rest = n1 % n2
print(
    "Soma = {} \n"
    "Subtraçãp = {} \n"
    "Multiplicação = {} \n"
    "Divisão = {} \n"
    "Potenciação = {} \n"
    "Divisão exata = {} \n"
    "Resto = {} \n".format(s, sub, m, div, exp, divEx, rest))