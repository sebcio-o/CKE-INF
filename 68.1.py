def is_solid(s):
    for char in s:
        if char != s[0]:
            return False
    return True 

c = 0
with open('./dane/68/dane_napisy.txt') as f:
    for line in f:
        l, p = line.split()
        if l == p and is_solid(l):
            c += 1
print(c)            
