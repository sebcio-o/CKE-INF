with open('./dane/66/trojki.txt') as f:
    for line in f:
        a, b, c = line.split()
        sum_ = 0
        for char in a + b:
            sum_ += int(char)
        if sum_ == int(c):
            print(a, b, c)
                
