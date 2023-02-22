with open('./dane/72/napisy.txt', 'r') as r:
    for line in r:
        a,b = line.split()

        for i in range(len(b), 0, -1):
            if b[:i] == a:
                print(a, b, b[i:])