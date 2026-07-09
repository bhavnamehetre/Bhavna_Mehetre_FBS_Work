# Write a program to find print the following Fibonacci series using
# functions: 1 1 2 3 5 8 n terms
def fibo(num):
    a = -1
    b = 1
    for i in range(num):
        c = a + b
        print(c,end=" ")
        a = b
        b = c
        
    
num = int(input("enter the number of terms:"))
res = fibo(num)
print(res)

