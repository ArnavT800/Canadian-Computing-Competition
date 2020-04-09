N = int(input())
s = []
for i in range(N):
    sunF = input().split(" ")
    s.append(sunF)

def rotate(s, N):
    f = []
    f = s
    for i in range(len(f)):
        for k in range(len(f)):
            f[i][k] = 0
            #print(f)
    for i in range(N):
        for k in range(N):
            f[k][-1] = s[i][k]
    return f

print(rotate(s, N))


   



    
    
    