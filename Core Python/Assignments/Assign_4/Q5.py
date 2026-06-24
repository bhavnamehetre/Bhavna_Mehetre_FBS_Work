# WAP to print Fibonacci series upto n.
a = -1
b = 1
n = int(input("enter the number:"))
for i in range(1,n):
    c = a + b
    print(c)
    a = b
    b = c 


