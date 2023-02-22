with open('./dane/75/tekst.txt') as r:
    data = r.read().strip().split()

for el in data:
    if el[0] == 'd' and el[0] == el[-1]:
        print(el)