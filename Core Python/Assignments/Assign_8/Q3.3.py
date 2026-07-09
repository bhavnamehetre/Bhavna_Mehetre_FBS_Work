#### Series 3  1^1 + 2^2 + 3^3+ ...... n^n
def exp(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + (i**i)
    return sum
n = int(input("enter the limit:"))
res = exp(n)
print(res)