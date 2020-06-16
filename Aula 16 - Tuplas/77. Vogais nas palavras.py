text = input('Digite uma palavra: ').lower().strip()
vog = ('a', 'e', 'i', 'o', 'u')
r = []
i = 0
for letter in range(len(text)):
    for v in range(len(vog)):
        if text[letter] == vog[v]:
            if r.count(text[letter]) == 0:
                r.append(text[letter])
            else:
                continue
        else:
            continue
print(r)

