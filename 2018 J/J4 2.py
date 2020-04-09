N = int(input())
data = []
for i in range(N):
    f  = input().split(" ")
    f = list(map(int, f))
    data.append(f)
tb = True
lr = True
if data[0][0] > data[0][1]:
    lr = False
if data[0][0] > data[1][0]:
    tb = False
result = []
if tb and lr:
    result = data

elif tb and not lr:
    for i in reversed(range(N)):
        #row = [data[j][i] for j in range(N)]
        #result.append(row)
        
        row = [data[j][i] for j in range(N)]
        result.append(row)

elif not tb and not lr:
    for i in reversed(range(N)):
        row = [data[i][j] for j in reversed(range(N))]
        result.append(row)
elif lr and not tb:
    for i in range(N):
        row = [data[j][i] for j in reversed(range(N))]
        result.append(row)


for i in result:
    print(*i)






