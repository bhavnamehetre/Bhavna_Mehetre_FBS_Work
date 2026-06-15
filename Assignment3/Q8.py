import random
u = "bhavna"
p = "bhavna@2005"
user = input("enter the username::")
passw = input("enter the password::")
if(u == user and p == passw):
    
    capcha = random.randint(1000,9999)
    print(capcha)
    c = int(input("enter the capcha::"))
    print("Login Successfull...!")
    # if(capcha == c):
    #     print("valid capcha...!")
    # else:
    #     print("Invalid capcha..!")
else:
    print("Invalid login...!")

