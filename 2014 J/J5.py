N = int(input())
s1 = input().split(" ")
s2 = input().split(" ")
dict = {}
dict2 = {}
selfPartner = False
for i in range(N):
    if s1[i] == s2[i]:
        selfPartner = True
    dict[s1[i]] = s2[i]
    dict2[s2[i]] = s1[i]

if dict == dict2 and selfPartner == False:
    print("good")
else:
    print("bad")


