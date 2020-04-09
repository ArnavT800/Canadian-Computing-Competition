N = int(input())
k = int(input())
sum = N
prod = N

for i in range(k):
    prod = prod*10
    sum+=prod


print(sum)
