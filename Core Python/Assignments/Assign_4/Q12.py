# Write a program to check if given number is Armstrong number or not.
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
# 4*4*4*4)

num = int(input("enter the number:"))
temp = num
sum = 0
c = 0
while(temp > 0):
    d = temp % 10
    temp = temp // 10
    print(d)
    c = c + 1
temp = num
while(temp > 0):
    d = temp % 10
    sum = sum + (d ** c)
    temp = temp // 10
if(sum == num):
    print("number is armstrong...!")
else:
    print("number is not armstrong...!")
