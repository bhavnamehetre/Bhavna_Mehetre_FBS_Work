# WAP to check if given number is Perfect Number.
sum = 0
num = int(input("enter the number:"))
for i in range(1,num):
    if(num % i == 0):
        sum = sum + i
if(sum == num):
    print("number is perfect...!")
else:
    print("number is not perfect..!")