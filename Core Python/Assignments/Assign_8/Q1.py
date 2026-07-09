# Write a program to calculate area of rectangle.
def area_rect(l,w):
 
    area = l * w
    return area
l = int(input("enter the length:"))
w = int(input("enter the width:"))
res = area_rect(l,w)
print("Area of rectangle is:",res)
