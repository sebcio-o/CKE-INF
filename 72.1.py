c = 0
para = None
with open('./dane/72/napisy.txt', 'r') as r:
    for line in r:
        a,b = line.split()
        alen = len(a)
        blen = len(b)
        if blen * 3 <= alen or alen * 3 <= blen:
            c += 1
            if para == None:
                para = line[:-1]

print(para)
print(c)