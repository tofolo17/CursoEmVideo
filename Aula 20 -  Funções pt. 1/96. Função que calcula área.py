def area(larg, comp):
    area = larg * comp
    print(f'A área de um terreno {larg} x {comp} é {area}.')


l = float(input('Digite a largura (m): '))
c = float(input('Digite o comprimento (m): '))
area(l, c)
