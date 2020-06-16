def insert(a, dictionary):
    for k, v in dictionary.items():
        a.writelines(f'{k}: ')
        a.writelines(f'{v:<10}')
    a.write('\n')


def readtxt(txtfile):
    try:
        file = open(txtfile, 'r')
        filepath = txtfile
        with open(filepath) as file:
            line = file.readline()
            cnt = 1
            while line:
                print("{}".format(line.strip()))
                line = file.readline()
                cnt += 1
    finally:
        file.close()
