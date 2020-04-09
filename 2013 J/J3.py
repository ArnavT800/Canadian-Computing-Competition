year = int(input()) + 1
year = str(year)
distinct = False
count = 0
while not distinct:
    for i in year:
        if year.count(i)>1:
            year = int(year)+1
            year = str(year)
            continue
        else:
            count+=1
    if count == len(year):
        distinct = True
        break
    else:
        count = 0

print(int(year))


    
    

