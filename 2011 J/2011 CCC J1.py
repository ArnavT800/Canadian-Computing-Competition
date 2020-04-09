print("How many antennas?")
a = float(input())
print("How many eyes?")
e = float(input())

T = False
V = False
G = False

if a<=6 and e >=2:
  V = True
  if a>=3 and e<=4:
    T = True
  elif a <=2 and e <=3:
    G = True
elif a>=3 and e <=4:
  T = True
  if a<=6 and e>=2:
    V = True
elif a<=2 and e<=3:
  G = True
  if a<=6 and e>=2:
    V = True


if T == True:
  print("TroyMartian")
if V == True:
  print("VladSaturnian")
if G == True:
  print("GraemeMercurian")
