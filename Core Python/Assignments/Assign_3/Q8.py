# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
# import random module
import random
u = "bhavna"
p = "bhavna@2005"

# accept input from user
user = input("enter the username::")
passw = input("enter the password::")

# check conditions
if(u == user and p == passw):
    # display result
    capcha = random.randint(1000,9999)
    print(capcha)
    c = int(input("enter the capcha::"))
    if(capcha == c):
        print("valid capcha...!")
    else:
        print("Invalid capcha..!")
    print("Login Successfull...!")
    
else:
    print("Invalid login...!")

