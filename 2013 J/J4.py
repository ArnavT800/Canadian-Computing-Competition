T = int(input())
C = int(input())
cList = []
for i in range(C):
    m = int(input())
    cList.append(m)
loopbreak = False
cList.sort()
time = 0
chore = 0

while not loopbreak:
    for i in range(len(cList)):
        if time + cList[i] <= T:
            time+=cList[i]
            chore+=1
            if time == T:
                loopbreak = True
                break
            
        else:
            loopbreak = True
            break
print(chore)



