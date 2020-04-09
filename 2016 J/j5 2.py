q = int(input())
n = int(input())
dmoj = list(map(int, input().split(" ")))
peg = list(map(int, input().split(" ")))
tot = 0
peg.sort()
dmoj.sort()
if q == 1:
    for i in range(len(dmoj)):
        tot+=max(dmoj[i], peg[i])
    print(tot)
else:
    peg = sorted(peg, reverse= True)
    for i in range(len(dmoj)):
        tot+= max(dmoj[i], peg[i])
    print(tot)

