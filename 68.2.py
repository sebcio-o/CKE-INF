c = 0
with open('./dane/68/dane_napisy.txt') as f:
    for line in f:
        l, p = line.split()
        if sorted(l) == sorted(p):
            c += 1
print(c)            
