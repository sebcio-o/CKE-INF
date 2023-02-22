with open('./dane/73/tekst.txt', 'r') as r:
    data = r.read().strip().split()

fword = ''
c = max_ = 0
for slowo in data:
    is_podslowo = False
    currmax = 0
    for el in slowo:
        if el not in "AEIOUY ":
            currmax += 1
            if currmax == max_:
                is_podslowo = True
        else:
            if max_ < currmax:
                max_ = currmax
                c = 0
                fword = slowo
            currmax = 0
    if max_ < currmax:
        max_ = currmax
        c = 0
        fword = slowo
    if is_podslowo:
        c += 1
    

print('SPOLGLOSKI:', max_)
print('SLOWA:', c)
print('PIERWSZE:', fword)
