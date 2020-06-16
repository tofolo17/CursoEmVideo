i = 1
notes = []
qtd = int(input('Qual a quantidade de avaliações? '))
while i < (qtd + 1):
    n = float(input('Digite o valor da {}° nota: '.format(i)))
    if n > 10:
        print('Essa nota não é válida! Deseja tentar novamente (S / N)?')
        resp = input(''.upper())
        if resp == 'S':
            continue
        else:
            exit()
    else:
        notes.append(n)
        i = i + 1
for n in notes:
    media = sum(notes)/len(notes)
if media < 5:
    print('Como sua média foi {:.1f}, você foi reprovado.'.format(media))
elif media > 6.9:
    print('Você teve uma média de {:.1f}. Parabéns, você foi aprovado!'.format(media))
else:
    print('Como voê teve uma média de {:.1f}, está de recuperação.'.format(media))