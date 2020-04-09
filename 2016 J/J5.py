question = int(input())

N = int(input())

dmojList = []
pegList = []

dmoj = input().split(" ")
peg = input().split(" ")
for i in range(N):
    pegList.append(int(peg[i]))
    dmojList.append(int(dmoj[i]))
pegList = sorted(pegList)
dmojList = sorted(dmojList)
pegReverse = sorted(pegList, reverse = True)
dmojReverse = sorted(dmojList, reverse = True)
sum = 0

if question ==1:
    for i in range(N):
        sum+=max(pegList[i], dmojList[i])
else:
    for i in range(N):
        sum+=max(pegReverse[i], dmojList[i])

print(sum)
