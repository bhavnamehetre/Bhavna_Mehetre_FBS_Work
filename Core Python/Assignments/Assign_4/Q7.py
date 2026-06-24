# WAP to print all integers upto n that aren’t divisible by 2 and 3.

num = int(input("enter the number:"))
for num in range(1,num):
    if(num % 2 != 0 and num % 3 != 0):
        print(num)


