with open('./dane/66/trojki.txt') as f:
    for line in f:
        a, b, c = line.split()
        a, b, c = int(a), int(b), int(c)
        if a**2 + b**2 == c**2:
            print(a, b, c)
            