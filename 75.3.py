def szyfruj(txt, a=5, b=2):
    x = ''
    for el in txt:
        x += chr(((ord(el) - 97) * a + b) % 26 + 97)
    return x


def s(x, y):
    for a in range(0, 26):
        for b in range(0, 26):
            if szyfruj(x, a, b) == y:
                print(f'{x} SZYFRUJACY ({a}, {b})')    

def d(x, y):
    for a in range(0, 26):
        for b in range(0, 26):
            if szyfruj(y, a, b) == x:
                print(f'{x} DESZYFRUJACY ({a}, {b})')    


with open('./dane/75/probka.txt') as r:
    for line in r:
        a, b = line.strip().split()
        s(a,b)
        d(a,b)
