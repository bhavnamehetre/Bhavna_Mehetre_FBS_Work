# WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start = int(input("enter the start:"))
stop = int(input("enter the stop:"))
for i in range(start,stop):
    if(i % 7==0 and i % 5==0):
        print(i)