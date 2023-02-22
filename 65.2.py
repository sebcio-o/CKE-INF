def is_nieskracalna(a, b):
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

c = 0
with open('./dane/65/dane_ulamki.txt') as f:
    for line in f:
        a, b = line.split()
        a, b = int(a), int(b)
        if is_nieskracalna(a, b):
            c += 1

print(c)