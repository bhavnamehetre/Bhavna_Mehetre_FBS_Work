# WAP to check if a given number is Armstrong number or not. For each task create separate functions.
def d(num):
    temp = num
    sum = 0
    count = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        count = count + 1
    temp = num
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)
    return sum
def arm1():
    num = int(input("Enter the number:"))
    if num == d(num) :
        print("number is armstrong....!")
    else:
        print("number is not armstrong...!")
arm1()