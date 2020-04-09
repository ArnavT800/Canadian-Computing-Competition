L = int(input())
num= []
sym = []
for i in range(L):
    string = input().split(" ")
    num.append(int(string[0]))
    sym.append(str(string[1]))


for i in range(len(num)):
    print(sym[i] * num[i])
    


