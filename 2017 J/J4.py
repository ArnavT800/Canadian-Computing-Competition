D = int(input())

days = D // 720
min = D % 720
total = days*31

if min >= 671:
    total+=31
elif min>= 591:
    total+=30
elif min>= 532:
    total+=29
elif min>=520:
    total+=28
elif min>=473:
    total+=27
elif min>=461:
    total+=26
elif min>=414:
    total+=25
elif min>=402:
    total+=24
elif min>=390:
    total+=23
elif min>=355:
    total+=22
elif min>=343:
    total+=21
elif min>=331:
    total+=20
elif min>=296:
    total+=19
elif min>=284:
    total+=18
elif min>=272:
    total+=17
elif min>=260:
    total+=16
elif min>=237:
    total+=15
elif min>=225:
    total+=14
elif min>=213:
    total+=13
elif min>=201:
    total+=12
elif min>=178:
    total+=11
elif min>=166:
    total+=10
elif min>=154:
    total+=9
elif min>=142:
    total+=8
elif min>=130:
    total+=7
elif min>=119:
    total+=6
elif min>=107:
    total+=5
elif min>=95:
    total+=4
elif min>=83:
    total+=3
elif min>=71:
    total+=2
elif min>=34:
    total+=1

print(total)




