def palin():
    num = int(input("enter the number:"))
    temp = num
    rev = 0
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
    sum = sum + rev
       
    if(sum == num):
        return True
    else:
        return False
res = palin()
print(res)