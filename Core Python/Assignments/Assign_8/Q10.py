# Write a program to check if entered year is a leap year or not.
def leap(year):
    if(year % 4 == 0):
        return year
year = int(input("enter the year:"))
res = leap(year)
print(res)