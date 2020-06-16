from random import randint
randons = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10) )
print(randons)
mm = sorted(randons)
print(mm[0], mm[-1])
