gender = input("enter the gender (M/F):")
age = int(input("enter the age:"))
if(gender == 'F'):
    if(age >= 18):
        print("Girl is eligible for marrige...!")
    else:
        print("Not eligible...!")
else:
    if(age >= 21):
        print("Boy is eligible for marrige...!")
    else:
        print("Not eligible...!")