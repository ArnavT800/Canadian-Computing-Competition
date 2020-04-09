s = input().split(" ")
num1, num2, num3, num4 = s
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)

print(0, num1, num1+num2, num1+num2+num3, num1+num2+num3+num4)
print(num1, 0, num2, num2+num3, num2+num3+num4)
print(num1+num2, num2, 0, num3, num3+num4)
print(num1+num2+num3,num2+num3,num3,0, num4 )
print(num1+num2+num3+num4, num2+num3+num4, num3+num4, num4, 0)
