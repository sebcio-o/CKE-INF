with open('./dane/73/tekst.txt', 'r') as r:
    data = r.read().strip().split()

c = 0
for i in range(0, len(data) - 1):
    a = data[i]
    for j in range(len(a) - 1):
        if a[j] == a[j + 1]:
            c += 1
            break
        
print(c)
