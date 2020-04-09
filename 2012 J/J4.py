s = int(input())
alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
word = input()
wordnew = []
for i in range(len(word)):
    shift = 3*(i+1)+s
    index = alph.index(word[i])
    wordnew.append(alph[index-shift])

string = ""
for i in wordnew:
    string += i
print(string)