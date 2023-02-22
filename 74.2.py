arr = []
printed = []
with open('./dane/74/hasla.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if line in arr and line not in printed:
            printed.append(line)
        arr.append(line)

for el in sorted(printed):
    print(el)
