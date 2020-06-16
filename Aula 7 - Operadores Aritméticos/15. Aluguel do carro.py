qKm = float(input('O carro percorreu quantos quilômetros? '))
qD = int(input('Qual a duração (em dias) do aluguel? '))
c = 60 * qD + 0.15 * qKm
print("O serviço custou: R${:.2f}".format(c))
