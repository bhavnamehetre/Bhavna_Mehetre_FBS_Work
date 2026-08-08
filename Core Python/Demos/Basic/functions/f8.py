
def arm(num):
    temp = num
    c = 0
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        c = c + 1
    print(c)
    temp = num
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d*d*d*d)

    
    if(sum == num):
        return True
    else:
        return False
num = 1634
res = arm(num)
print(res)

    
