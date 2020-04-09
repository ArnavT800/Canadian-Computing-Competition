L = int(input())
num = []
sym = []
for i in range(L):
    inp = input().split(" ")
    num.append(int(inp[0]))
    sym.append(inp[1])

for i in range(len(num)):
    print(sym[i] * num[i])