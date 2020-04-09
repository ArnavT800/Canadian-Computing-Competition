M = int(input())
dict = {}
dict2 = {}
time  = 0
for i in range(M):
    msg = input().split(" ")
    if msg[0] == "W":
        time+= int(msg[1])
        for k in dict:
            dict[k] += int(msg[1]) -1     
            
    elif msg[0] == "R":
        if int(msg[1]) not in dict:
            dict[int(msg[1])] = 0
            for k in dict:
                dict[k]+=1
            time+=1
    else:
        if int(msg[1]) in dict2:
            dict2[int(msg[1])] += dict[int(msg[1])]
        else:
            dict2[int(msg[1])] = dict[int(msg[1])]
        del dict[int(msg[1])]
        for k in dict:
            dict[k]+=1
        time+=1

for i in dict:
    dict2[i] = -1
for key, val in sorted(dict2.items()):
    print(key, val)


       

