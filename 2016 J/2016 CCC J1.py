wl = []

for i in range(6):
    wl.append(input())



if wl.count("W") >=5:
    print("1")
elif wl.count("W") >=3:
    print("2")
elif wl.count("W") >=1:
    print("3")
else:
    print("-1")
    
