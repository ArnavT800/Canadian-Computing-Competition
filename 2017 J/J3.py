start = input().split(" ")
end = input().split(" ")
c = int(input())

startX = int(start[0])
startY = int(start[1])
endX = int(end[0])
endY = int(end[1])

distance = abs(startX-endX) + abs(startY-endY)

remainingT = c - distance
print(distance)
print(remainingT)

if remainingT <0:
    print("N")
elif remainingT == 0:
    print("Y")
else:
    if remainingT %2 == 0:
        print("Y")
    else:
        print("N")



