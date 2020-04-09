w = input()
i = 0
ll = []
wl = []
while i<len(w):
    wl = []
    #ll = []
    for k in range(i, (len(w))):
        wl.append(w[k])
        if wl[0:] == wl[::-1]:
            ll.append(len(wl))
    i+=1

print(max(ll))