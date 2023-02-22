B = 2**2 * 3**2 * 5**2 * 7**2 * 13
s = 0
with open('./dane/66/dane_ulamki.txt') as f:
    for line in f:
        a, b = line.split()
        s += (int(a) * B) / int(b)     

print(int(s))