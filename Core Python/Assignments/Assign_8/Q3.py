# Write a program to find sum of following series using functions :
# 1+ 2 + 3 + 4+..... + n
###### Series 1
def sum1(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
n = int(input("enter the limit:"))
res = sum1(n)
print(res)







