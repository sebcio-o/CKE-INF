from collections import Counter

data = []
with open('./dane/68/dane_napisy.txt') as f:
    for i in f:
        a, b = i.split()
        data.append(''.join(sorted(a)))
        data.append(''.join(sorted(b)))

c = Counter(data) 
m = max(c, key=lambda x: c[x])
print(m, c[m])