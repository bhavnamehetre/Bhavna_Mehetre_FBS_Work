# WAP to print sum of series upto n.
sum = 0
start = int(input("enter the start point:"))
stop = int(input("enter the stop point:"))
for i in range(start,stop+1):
    sum = sum + i
print(sum)
