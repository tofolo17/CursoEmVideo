from Utilidades.Personalização import *
from Utilidades.Validação import *
from Utilidades.Texto import *
from time import sleep
prov = dict()
data = list()
resp = 0
while resp != 3:
    titulo('MENU PRINCIPAL', 30)
    print(f'{amarelo("[1]")} {azul("Ver pessoas cadastradas")}')
    print(f'{amarelo("[2]")} {azul("Cadastrar pessoas")}')
    print(f'{amarelo("[3]")} {azul("Sair")}')
    mostralinha()
    resp = validaropcoes(3)
    if resp == 1:
        titulo('PESSOAS CADASTRADAS', 30)
        readtxt('Cadastrados.txt')
    elif resp == 2:
        titulo('NOVO CADASTRO', 30)
        prov['Nome'] = validarstr('Nome: ')
        prov['Idade'] = validarint('Idade: ')
        cads = open('Cadastrados.txt', 'a')
        insert(cads, prov)
        cads.close()
        print(f'Novo registro de {prov["Nome"]} adicionado.')
print(f'{azul("Saindo do sistema...".upper().center(30), True)}')
sleep(1)
print(f'{azul("Volte sempre".upper().center(30), True)}')
