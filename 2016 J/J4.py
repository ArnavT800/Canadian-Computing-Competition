dep = input().split(":")
if dep[0][0] == "0":
    hour = int(dep[0][1])
else:
    hour = int(dep[0][0]+dep[0][1])
if dep[1][0] == "0":
    min = int(dep[1][1])
else:
    min = int(dep[1][0]+dep[1][1])
i = 0

while i <= 120:
    if min == 60:
        min = 0
        hour+=1
    if hour==24:
        hour = 0
    if i ==120:
        break
    if (7<=hour<10 or 15<=hour<19):
        i+=0.5
    else:
        i+=1
    min+=1

if i == 120.5:
    if min ==60:
        min = 0
        hour+=1
        min+=1
    if hour ==24:
        hour = 0




if min ==60:
    min = 0
    hour+=1
if hour ==24:
    hour = 0


   
   
if hour<10:
    hour = "0"+str(hour)
else:
    hour = str(hour)
if min<10:
    min = "0"+str(min)
else:
    min = str(min)

print(hour+":"+min)