n = int(input())
cod = []
for i in range(n):
    inp = list(map(str, input()))
    cod.append(inp)
for i in range(len(cod)):
    sym = []
    num = []
    count = 0
    o = ""
    for j in range(len(cod[i])):
        if j == 0:
            sym.append(cod[i][j])
            count = 1
        else:
            if j == len(cod[i])-1:
                if cod[i][j] == cod[i][j-1]:
                    count+=1
                    num.append(count)
                else:
                    num.append(count)
                    count = 1
                    sym.append(cod[i][j])
                    num.append(count)

            elif cod[i][j] == cod[i][j-1]:
                count+=1
            elif cod[i][j] != cod[i][j-1]:
                num.append(count)
                count = 1
                sym.append(cod[i][j])
    o = ""
    for m in range(len(sym)):
        o+=str(num[m])
        o+=" "
        o+=sym[m]
        o+=" "
    print(o)
        


