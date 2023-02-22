def s(txt, a=5, b=2):
    x = ''

    for el in txt:
        x += chr(((ord(el) - 97) * a + b) % 26 + 97)

    return x


with open('./dane/75/tekst.txt') as r:
    data = r.read().strip().split()

for el in data:
    if len(el) < 10:
        continue
    print(s(el))