c = 0
with open('./dane/74/hasla.txt', 'r') as f:
    for line in f:
        line = line.strip()
        for i in range(len(line) - 3):
            ciag = sorted(ord(el) for el in line[i:i + 4])
            if ciag[0] + 1 == ciag[1] and ciag[1] + 1 == ciag[2] and ciag[2] + 1 == ciag[3]:
                c += 1
                break
print(c)