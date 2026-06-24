# Write a program to check whether the triangle is equilateral, isosceles or scalenetriangle.

a = int(input("enter the first angle::"))
b = int(input("enter the second angle::"))
c = int(input("enter the third angle::"))
if(a == b == c):
    print("triangle is equilateral..!")
elif(a == b or a == c):
    print("triangel is isoscalence....!")
else:
    print("triangle is scalence...!")


