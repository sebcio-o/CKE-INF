def getNieksracalnyLicznik(a, b):
    m = a
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            m = a // i
    return m

s = 0
with open('./dane/65/dane_ulamki.txt') as f:
    for line in f:
        a, b = line.split()
        a, b = int(a), int(b)
        s += getNieksracalnyLicznik(a, b)     

print(s)