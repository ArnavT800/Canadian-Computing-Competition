D = int(input())

table = [
    [34],
    [11,23,35,47,59],
    [10,22,34,46,58],
     [21,33,45,57],
     [20,32,44,56],
     [31,43,55],
     [30,42,54],
     [41,53],
     [40,52],
     [51], 
     [],
     [11]
]

numHours = D // 60

numTwelveHourCycles = numHours // 12
totalTableLength = 31
total = totalTableLength * numTwelveHourCycles

leftOverHours = numHours % 12
leftOverMinutes = D % 60

for i in range(leftOverHours):
    total += len(table[i])

for elem in table[leftOverHours]:
    if elem <= leftOverMinutes:
        total += 1

print(total)
