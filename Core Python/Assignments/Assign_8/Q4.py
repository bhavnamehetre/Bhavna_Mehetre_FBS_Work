def odd(start,stop):
    sum = 0
    
    for i in range(start,stop):
        if(i % 2 != 0):
            sum = sum + i
    return sum
start = int(input("enter the start point:"))
stop = int(input("enter the stop point:"))
res = odd(start,stop)
print("Sum is:",res)


        