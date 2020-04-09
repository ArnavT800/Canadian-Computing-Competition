w = input()
lens  = []
for i in range(len(w)):
    s = ""
    s+=w[i]
    for j in range(i+1, len(w)):
        s+=w[j]
        if s==s[::-1]:
            lens.append(len(s))
print(max(lens))
