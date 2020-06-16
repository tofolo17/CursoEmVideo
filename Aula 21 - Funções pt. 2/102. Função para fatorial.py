def factorial(number, show=0):
    fac = 1
    for x in range(number, 0, -1):
        if show:
            print(f'{x} * ' if x != 1 else f'{x} = ', end='')
        fac *= x
    return fac


n = int(input('Digite um número: '))
print(factorial(n, True))
