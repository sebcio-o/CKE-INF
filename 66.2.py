def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

with open('./dane/66/trojki.txt') as f:
    for line in f:
        a, b, c = line.split()
        a, b, c = int(a), int(b), int(c)
        if is_prime(a) and is_prime(b) and c == a * b:
            print(a, b, c)
                
