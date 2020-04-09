N = int(input())
b = input().split(" ")
b = list(map(int, b))
b.sort()
b2 = reversed(b)

start, end = 0, N-1
startList = []
