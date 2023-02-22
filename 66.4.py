curr = all_ = longest = 0
with open('./dane/66/trojki.txt') as f:
    for line in f:
        a, b, c = line.split()
        a, b, c = int(a), int(b), int(c)
        if a + b >= c and a + c >= b and b + c >= a:
            curr += 1
            all_ += 1
            if longest < curr:
                longest = curr
        else:
            curr = 0

print(all_, longest)
            
