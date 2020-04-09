spots  = [(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5), (4, -5), (5, -5), (5, -4), (5, -3), (6, -3), 
(7, -3), (7, -4), (7, -5), (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7), (0, -7), (-1, -7),
(-1, -6), (-1, -5)]
danger = False
spots = list(map(list, spots))
x = [-1, -5]
inp = "0"
while inp[0] != "q" and not danger:
    inp = input().split(" ")
    if  inp[0] == "q":
        break
    elif inp[0] == "d":
        for i in range(int(inp[1])):
            x[1]-=1
            if x in spots:
                danger = True
        x = list(map(str, x))
        x = " ".join(x)
        if danger:
            print(x, "DANGER")
            break
        else:
            print(x, "SAFE")
    elif inp[0] == "r":
        for i in range(int(inp[1])):
            x[0]+=1
            if x in spots:
                danger = True
        x = list(map(str, x))
        x = " ".join(x)
        if danger:
            print(x, "DANGER")
            break
        else:
            print(x, "SAFE")
    elif inp[0] == "l":
        for i in range(int(inp[1])):
            x[0]-=1
            if x in spots:
                danger = True
        x = list(map(str, x))
        x = " ".join(x)
        if danger:
            print(x, "DANGER")
            break
        else:
            print(x, "SAFE")
    elif inp[0] == "u":
        for i in range(int(inp[1])):
            x[1]+=1
            if x in spots:
                danger = True
        x = list(map(str, x))
        x = " ".join(x)
        if danger:
            print(x, "DANGER")
            break
        else:
            print(x, "SAFE")
    x = list(map(int, x))
    print(x)


        
