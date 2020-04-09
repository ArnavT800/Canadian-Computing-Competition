cont = True
while cont:
    inp = input().split(" ")
    if int(inp[0]) == 7:
        cont = False
        break
    elif int(inp[0]) == 1:
        if inp[1] == "A":
            a = int(inp[2])
        else:
            b = int(inp[2])
    elif int(inp[0]) == 2:
        if inp[1] == "A":
            print(a)
        else:
            print(b)
    elif int(inp[0]) == 3:
        if inp[1] == "A":
            if inp[2] == "B":
                a = a+b
            else:
                a = a+a
        else:
            if inp[2] == "A":
                b = b+a
            else:
                b = b+b
    elif int(inp[0]) == 4:
        if inp[1] == "A":
            if inp[2] == "B":
                a = a*b
            else:
                a= a*a
        else:
            if inp[2] == "A":
                b = a*b
            else:
                b = b*b
    elif int(inp[0]) == 5:
        if inp[1] == "A":
            if inp[2] == "B":
                a = a-b
            else:
                a= a-a
        else:
            if inp[2] == "A":
                b = b-a
            else:
                b = b-b
    elif int(inp[0]) == 6:
        if inp[1] == "A":
            if inp[2] == "B":
                a = int(a/b)
            else:
                a= a/a
        else:
            if inp[2] == "A":
                b = int(b/a)
            else:
                b = b/b


