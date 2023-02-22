import re

c = 0
with open('./dane/74/hasla.txt', 'r') as f:
    for line in f:
        if re.fullmatch(r'([0-9])+', line.strip()):
            c += 1
            
print(c)