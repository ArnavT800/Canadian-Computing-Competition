def searchForPath(cur, stepsTaken, curPath):
    if (cur, stepsTaken) in dp:
        return dp[(cur, stepsTaken)]
    if cur == end and stepsTaken == steps:
        return True

    if stepsTaken == steps and cur != end:
        return False
    for rule in mappings:
        startIndex = cur.find(rule[0], 0)
        while startIndex != -1:
            transformedString = cur[0:startIndex] + rule[1] + cur[startIndex + len(rule[0]):]
            curPath.append([rule[2], startIndex + 1, transformedString])
            if searchForPath(transformedString, stepsTaken + 1, curPath):
                return True
            curPath.pop()
            startIndex = cur.find(rule[0], startIndex + 1)
    dp[(cur, stepsTaken)] = False
    return False


mappings = []
dp = {}
for i in range(3):
    start, end = input().split(' ')
    mappings.append([start, end, i + 1])

steps, start, end = input().split(' ')
steps = int(steps)

curPath = list()
searchForPath(start, 0, curPath)
for i in curPath:
    print(*i)