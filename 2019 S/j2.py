prime = set()
isPrime = True
for i in range(2, 10000):
    for k in range(2, i):
        isPrime = True
        if i%k==0:
            isPrime = False
            break
        else:
            continue
    if isPrime:
        prime.add(i)
sums = []
T = int(input())
for i in range(T):
    s = int(input())*2
    for k in prime:
        diff = s - k
        if diff not in prime:
            continue
        else:
            sums.append([diff, k])
            break
for i in sums:
    print(*i)          


