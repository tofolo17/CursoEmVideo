from random import randint


def higher():
    mai = i = 0
    for x in range(0, randint(1, 10), 1):
        rnd = randint(1, 10)
        print(f'{rnd} ', end='')
        i += 1
        if rnd == 0:
            rnd = mai
        else:
            if rnd > mai:
                mai = rnd
    print()
    print(f'{i} valores foram analisados.')
    print(f'O maior valor é {mai}.')


higher()
