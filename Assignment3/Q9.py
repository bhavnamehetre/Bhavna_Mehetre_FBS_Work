# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

# Accept input from the user.
m1 = int(input("enter the marks for 1 sub::"))
m2 = int(input("enter the marks for 2 sub::"))
m3 = int(input("enter the marks for 3 sub::"))
m4 = int(input("enter the marks for 4 sub::"))
m5= int(input("enter the marks for 5 sub::"))
total_mar = m1 + m2 + m3 + m4 + m5

per = total_mar / 500 * 100
if(per >= 90):
    print("Class first..!")
elif(per >= 75):
    print("Class second..!")
elif(per >= 60):
    print("Class Third..!")
elif(per >= 35):
    print("Pass..!")
else:
    print("Fail...!")

