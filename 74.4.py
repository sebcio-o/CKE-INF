c = 0
with open('./dane/74/hasla.txt', 'r') as f:
    for line in f:
        line = line.strip()
        uppercase = lowercase = numeric = False
        for el in line:
            if el.isnumeric():
                numeric = True
            elif el.capitalize() == el:
                uppercase = True
            else:
                lowercase = True
        if uppercase and lowercase and numeric:
            c += 1
print(c)