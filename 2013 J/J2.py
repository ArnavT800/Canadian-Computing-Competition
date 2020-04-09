rotate = ["I", "O", "S", "H", "Z", "X", "N"]
word = input()
possible = True
for i in word:
    if i not in rotate:
        possible = False

if possible:
    print("YES")
else:
    print("NO")
