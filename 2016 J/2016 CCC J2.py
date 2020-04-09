row1 = input()
row1 = row1.split(" ")
row2 = input()
row2 = row2.split(" ")
row3 = input()
row3 = row3.split(" ")
row4 = input()
row4 = row4.split(" ")

row1sum = 0
row2sum = 0
row3sum = 0
row4sum = 0
for i in range(len(row1)):
    row1sum +=int(row1[i])
    row2sum +=int(row2[i])
    row3sum +=int(row3[i])
    row4sum += int(row4[i])

col1sum = int(row1[0]) + int(row2[0]) + int(row3[0]) +int(row4[0])
col2sum = int(row1[1]) + int(row2[1]) + int(row3[1]) +int(row4[1])
col3sum = int(row1[2]) + int(row2[2]) + int(row3[2]) +int(row4[2])
col4sum = int(row1[3]) + int(row2[3]) + int(row3[3]) +int(row4[3])




if row1sum == row2sum == row3sum == row4sum:
    if col1sum == col2sum == col3sum == col4sum:
        print("magic")
    else:
        print("not magic")
else:
    print("not magic")





