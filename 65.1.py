max_ = ['', '', 12_001]
with open('./dane/65/dane_ulamki.txt') as f:
    for line in f:
        a, b = line.split()
        a, b = int(a), int(b)
        x = a / b
        if max_[2] > x or max_[2] == x and b < max_[1]:
            max_ = [a, b, x]

print(max_[0], max_[1])