# Write a program to find sum of digits of a number.
def sum(num):
    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + d
    return sum
num = int(input("enter the number:"))
res = sum(num)
print("The sum of digit is:",res)
