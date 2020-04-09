w = input()
vowel = ["a", "e", "i", "o", "u"]
const1 = ["b", "c"] #a
const2 = ["d", "f", "g"] #e 
const3 = ["h", "j", "k", "l"]#i
const4 = ["m","n","p","q","r"]#o
const5 = ["s", "t", "v", "w","x", "y","z"]#u
newW = ""
for i in w:
    if i in vowel:
        newW+=i
    else:
        if i in const1:
            newW+=i
            newW+="a"
            if i ==const1[-1]:
                newW+=const2[0]
            else:
                index = const1.index(i)
                newW+=const1[index+1]
        elif i in const2:
            newW+=i
            newW+="e"
            if i ==const2[-1]:
                newW+=const3[0]
            else:
                index = const2.index(i)
                newW+=const2[index+1]
        elif i in const3:
            newW+=i
            newW+="i"
            if i ==const3[-1]:
                newW+=const4[0]
            else:
                index = const3.index(i)
                newW+=const3[index+1]
        elif i in const4:
            newW+=i
            newW+="o"
            if i ==const4[-1]:
                newW+=const5[0]
            else:
                index = const4.index(i)
                newW+=const4[index+1]
        elif i in const5:
            newW+=i
            newW+="u"
            if i ==const5[-1]:
                newW+="z"
            else:
                index = const5.index(i)
                newW+=const5[index+1]
print(newW)