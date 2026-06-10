# Write a program to check given username and password is right or wrong.

user="bhavna"
password="bhavna@123"

# Accepts input from the user.
username=input("enter the username:")
p=input("enter the password:")

# perfrom operations and display result.
if(username==user and p==password):
    print("Login Successfully....!")
else:
    print("Invalid.....!")
