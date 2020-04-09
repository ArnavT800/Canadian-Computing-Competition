l = 2
s = int(input())
e = int(input())
diff = s-e
while True:
  if s-e <0:
    break
  else:
    diff = s-e
    s = e
    e = diff
    l+=1
print(l)

