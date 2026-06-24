num = int(input("enter the three digit number::"))
temp = num
d1 = temp % 10
temp = temp // 10

d2 = temp % 10
temp = temp // 10

d3 = temp % 10
temp = temp // 10

sum = d1*100 + d2*10+ d3
if(sum == num ):
    print("number is palindrom...!")
else:
    print("not...!")

