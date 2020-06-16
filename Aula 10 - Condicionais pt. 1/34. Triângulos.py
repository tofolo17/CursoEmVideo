i = 1
list1 = []
while i < 4:
    side = int(input("Insira a medida do {}° lado: ".format(i)))
    list1.append(side)
    i = i + 1
a = int(list1[0])
b = int(list1[1])
c = int(list1[2])
if (abs(b-c) < a < (b+c)) and (abs(a-c) < b < (a+c)) and (abs(a-b) < c < (a+b)):
    print('Dá pra fazer um triângulo')
else:
    print('Nem dá')

