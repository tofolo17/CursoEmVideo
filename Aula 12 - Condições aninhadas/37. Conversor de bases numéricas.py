n = int(input('Digite o número a ser convertido: '))
print('[1] - Converter para BINÁRIO')
print('[2] - Converter para OCTAL')
print('[3] - Converter para HEXADECIMAL')
opt = int(input('Sua opção: '))
if opt == 1:
    print(bin(n)[2:])
elif opt == 2:
    print(oct(n)[2:])
elif opt == 3:
    print(hex(n)[2:])
else:
    print('Trolla não cara.')
