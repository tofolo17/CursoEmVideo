from random import choice

# SE QUISER DEIXAR TUDO NO CENTRO DA TELA, USE A VARIAVEL "CENTER" PARA ISSO
# AUMENTE PARA IR PARA DIREITA
# DIMINUA PARA IR PARA ESQUEDA
# NAO USE VALORES ALTOS, OU BUGS OCORRERÃO

center = 0


# ---------------------------------------------------------------------------


# ------------------       NAO USE ACENTOS NAS LETRAS!


def ClearScreen():
    print("\n" * 30)


def ChangeLetter():
    global letra, palavra, letrasEncontradas
    return_tmp = ""
    for p, l in enumerate(palavra):
        if l == letra:
            return_tmp += l
        else:
            return_tmp += letrasEncontradas[p]
    return return_tmp


def ShowFoundLetters():
    global letrasEncontradas
    print((center - len(letrasEncontradas) + 5) * " ", end="")
    for l in letrasEncontradas:
        print("\033[4;32m", end="")
        if(l in " _"):
            print("\033[m", end="")
            print("\033[1;30m", end="")
        print(l + "\033[m\033[1;30m ", end="")
    print("\n" * 9)


def ShowLettersUsed():
    global letrasUsadas
    print((center - 2) * " " + "\033[1;30mLETRAS USADAS")
    print((center - int(len(letrasUsadas) / 2) + 5) * " ", end="")
    for l in letrasUsadas[0:-2]:
        print("\033[1;31m", end="")
        if(l==","):
            print("\033[1;30m", end="")
        print(l, end="")
    print("\n")


def DrawBody():
    global partesDoCorpo, center, error
    if (error == 1):
        partesDoCorpo[0] = "O"  # cabeca
    elif (error == 2):
        partesDoCorpo[1] = "|"  # tronco cima
    elif (error == 3):
        partesDoCorpo[2] = "|"  # tronco baixo
    elif (error == 4):
        partesDoCorpo[3] = "/"  # perna esqueda
    elif (error == 5):
        partesDoCorpo[4] = " \\"  # perna direita
    elif (error == 6):
        partesDoCorpo[5] = "/"  # braco esquedo
    elif (error == 7):
        partesDoCorpo[6] = "\\"  # braco direito

    print(center * " " + "\033[1;30m   ____ ")
    print(center * " " + "\033[1;30m  /    |")
    print(center * " " + "\033[1;30m /     \033[1;31m" + partesDoCorpo[0])
    print(center * " " + "\033[1;30m|     \033[1;31m" + partesDoCorpo[5] + partesDoCorpo[1] + partesDoCorpo[6])
    print(center * " " + "\033[1;30m|      \033[1;31m" + partesDoCorpo[2])
    print(center * " " + "\033[1;30m|     \033[1;31m" + partesDoCorpo[3] + partesDoCorpo[4])
    print(center * " " + "\033[1;30m|\n")


def UpdateScreen():
    ClearScreen()
    print((center - 6) * " " + "\033[1;31m<ESPAÇO IGUAL A HÍFEN>" + "\n" * 6)
    ShowLettersUsed()
    DrawBody()
    ShowFoundLetters()


# --------------------------------------------------------------------------------------------

error = 0

aux = "abcdefghijklmnopqrstuvwxyz-"
partesDoCorpo = [" ", " ", " ", " ", " ", " ", " "]
letrasUsadas = ""

# palavra = "teste"

print((center - 4) * " " + "\033[1;30m[1] Jogar sozinho\n" + (center - 4) * " " + "[2] Jogar com alguém")

tipo = int(input((center - 4) * " " + "Opção> "))

if (tipo == 1):

    # Voce pode adicionar mais palavras se quiser ----------------

    # Nomes de animais
    ani = ["raposa", "tubarao", "cobra", "jabuti", "baleia", "cachorro", \
           "gato", "peixe", "arraia", "alce", "pinguim", "rato", "avestruz", "macaco", \
           "boi", "vaca"]

    # Nomes de frutas
    fru = ["banana", "laranja", "uva", "morango", "manga", "melancia", "pera", \
           "jaca", "cereja", "goiaba", "acerola", "abacate", "cacau", "caqui", "carambola", \
           "groselha", "jabuticaba", "jambo", "kiwi", "amora", "abacaxi"]

    print((center - 4) * " " + "[1] Animais\n" + (center - 4) * " " + "[2] Frutas")

    tipo = int(input((center - 4) * " " + "Opção> "))

    if (tipo == 1):
        palavra = choice(ani)
    else:
        palavra = choice(fru)

else:
    palavra = input(center * " " + "Palavra> ").lower().replace(" ", "-")

letrasEncontradas = "_" * len(palavra)
UpdateScreen()

# codigo principal
while letrasEncontradas != palavra and error < 7:
    try:
        letra = input(center * " " + "\033[1;30mLetra> ")[0].lower()
    except:
        letra = ""

    if(letra == " "):
        letra = "-"

    if (letra not in letrasUsadas and letra in aux):
        letrasUsadas += letra + ", "
        if (letra in palavra):
            letrasEncontradas = ChangeLetter()
        else:
            error += 1

    UpdateScreen()

ClearScreen()

if (error == 7):
    print(center * " " + "\033[4;31mVocê perdeu!")
    print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "\033[m\033[1;30ma palavra era\033[1;31m", palavra, "\n" * 15)
else:
    print(center * " " + "\033[4;32mVocê ganhou!")
    print((center - int(len("a palavra era " + palavra) / 2) + 5) * " " + "\033[m\033[1;30ma palavra era\033[1;32m", palavra, "\n" * 15)






