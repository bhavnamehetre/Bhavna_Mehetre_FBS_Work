# WAP to print all numbers in a range divisible by a given number.
start = int(input("enter the start point:"))
stop = int(input("enter the stop point:"))
num = int(input("enter the number:"))
for i in range(start,stop):
    if(i % num == 0):
        print(i)