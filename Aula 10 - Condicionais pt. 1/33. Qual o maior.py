list1 = []

num = int(input("Digite a quantidade de números a se comparar: "))

for i in range(1, num + 1):
    ele = int(input("Insira o {}° número: ".format(i)))
    list1.append(ele)

print("O maior número é:", max(list1))
print("O menor número é:", min(list1))
