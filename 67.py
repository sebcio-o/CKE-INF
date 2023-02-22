print('ZAD 1')
def f(n):
    i, j = 1, 1
    for _ in range(1, n):
        i, j = j, i + j
    return j

print(f(10), f(20), f(30), f(40))

print('ZAD 2')
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(1, 41):
    fi = f(i)
    if is_prime(fi):
        print(fi)

print('ZAD 3')
arr = []
for i in range(1, 41):
    fi = f(i)
    arr.append(bin(fi)[2:])

longest_fib = len(arr[-1])
for fib in arr:
    for _ in range(longest_fib - len(fib) ):
        print('0', end='')
    for char in fib:
        print(char, end='')
    print()

    
print('ZAD 4')
for fib in arr:
    c= 0
    for char in fib:
        if char == '1':
            c += 1
    if c == 6:
        print(fib)