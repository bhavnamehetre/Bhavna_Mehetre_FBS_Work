# Write a program find reverse of a number.
def rev(num):
    temp = num
    rev = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    return rev
num = int(input("enter the number:"))
res = rev(num)
print("The reverse number is:",res)