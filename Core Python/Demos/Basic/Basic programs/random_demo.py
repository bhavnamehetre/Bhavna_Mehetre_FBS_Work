import random
c = int(input("enter the captcha::"))
captcha=random.randint(1000,9999)
if(c == captcha):
    print("login...!")
else:
    print("not...!")