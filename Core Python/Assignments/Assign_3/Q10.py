# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

# Accept input from the user.
gender = input("enter the gender(Male/Female):")
age = int(input("enter the age::"))
if(gender == "F"):
    if(age >= 18):
        print(" Girl Eligible for marrige...! ")
    else:
        print("not eligible...!")
else:
    if(age >= 21):
        print("boy eligible for marrige...!")
    else:
        print("kama lo pehle..!")