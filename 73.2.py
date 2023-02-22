from collections import Counter

with open('./dane/73/tekst.txt', 'r') as r:
    data = r.read().strip().split()

c = Counter(''.join(i for i in data))
s = 1 + sum(c.values())
for k,v in sorted(c.items()):
    print(f'{k}: {v} ({round((v / s) * 100,2)}%)')
