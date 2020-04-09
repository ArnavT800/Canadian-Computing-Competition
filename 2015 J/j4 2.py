m = int(input())
t = 0
d = {}
s = {}
for i in range(m):
    inp = input().split(" ")
    inp[1] = int(inp[1])
    w = False
    if inp[0] == "W":
        for k, v in d.items():
            if k in s:
                continue
            else:
                d[k]+=inp[1]-1
    elif inp[0] == "S":
        s[inp[1]] = d[inp[1]]
        for k, v in d.items():
            if k in s:
                continue
            else:
                d[k]+=1
        
    else:
        if inp[1] not in d:
            d[inp[1]] = 0
        if inp[1] in s:
            del s[inp[1]]
        for k, v in d.items():
            if k in s:
                continue
            else:
                d[k]+=1
 
        
                
for k in d:
    if k not in s or d[k] > s[k]:
        s[k] = -1
s = sorted(s.items())
for i in range(len(s)):
    print(s[i][0], s[i][1])



    

        

