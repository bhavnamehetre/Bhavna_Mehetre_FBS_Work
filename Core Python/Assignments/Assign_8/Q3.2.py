###### Series 2    1!+ 2! + 3! + 4!+..... + n!
def fact(num):
    fact = 1
    sum = 0
    for i in range(1,num+1):
        fact = fact * i
        sum = sum + fact
    return sum
num = int(input("enter the limit:"))
res = fact(num)
print(res)