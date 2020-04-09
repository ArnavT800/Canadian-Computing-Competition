h = int(input())
M = int(input())

t = 1
A = 0
switch = 0


while t <= M and switch==0:
  A = (-6*(t**4)) + (h*(t**3)) + (2*(t**2)) + (t)
  if A <= 0:
    print("The balloon first touches ground at hour:")
    print(t) 
    switch+=1  
  else:
    t+=1

if switch==0:
  print("The balloon does not touch ground in the given time.")


