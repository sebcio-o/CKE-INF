max_ = 0
arr = []
with open('./dane/72/napisy.txt', 'r') as r:
    for line in r:
        line = line.strip()
        a,b = line.split()
        aidx = len(a) - 1
        bidx = len(b) - 1

        curr_max = 0
        while aidx > 0 and bidx > 0:
            if b[bidx] == a[aidx]:
                curr_max += 1
            else:
                break
            bidx -= 1
            aidx -= 1
        
        if curr_max > max_:
            max_ = curr_max
        if max_ == curr_max:
            arr.append(line)

print(max_)
for i in arr:
    print(i)