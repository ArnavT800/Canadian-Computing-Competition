cont = True
arr = []
diffList = []
finalList = []
while cont:
    diffList = []
    inp = input()
    if inp == "0":
        cont = False
        break
    arr = list(map(int, inp.split(" ")))
    for i in range(arr[0]):
        if i+2<=arr[0]:
            diff = arr[i+2]- arr[i+1]
            if diff not in diffList:
                diffList.append(diff)
            else:
                continue
        else:
            break
    finalList.append(diffList)

#for i in range(len(finalList)):
    #print(len(finalList[i]))
print(finalList)


         