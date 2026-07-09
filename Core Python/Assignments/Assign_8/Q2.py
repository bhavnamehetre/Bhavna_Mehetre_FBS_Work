# Write a program to calculate area of circle.
def area_cir(r):
    area = 3.14*r*r
    return area
radius = int(input("enter the radius:"))
res = area_cir(radius)
print("Area of circle is:",res)

