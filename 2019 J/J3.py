N = int(input())
result = []
c = 0
for i in range(N):
    final = []
    sym = []
    num = []
    s = input()
    c=0
    for i in range(len(s)):
        if i+1 != len(s):
            if s[i] == s[i+1]:
                c+=1
            else:
                sym.append(s[i])
                num.append(c+1)
                c=0
        else:
            sym.append(s[i])
            num.append(c+1)
            c = 0
    for i in range(len(sym)):
        final.append(num[i])
        final.append(sym[i])
    result.append(" ".join(map(str, final)))

for i in result:
    print(i)









    


    



    
        

        
            

