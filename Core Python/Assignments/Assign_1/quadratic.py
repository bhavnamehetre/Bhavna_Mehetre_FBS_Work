# Program to Find the Roots of a Quadratic Equation.

# Accepts input from the user

a=int(input('Enter the value for a::'))
b=int(input('Enter the value for b::'))
c=int(input('Enter the value for c::'))

# perform operations
d=b**2-(4*a*c)
r1 = (- b + (d**0.5))//(2 * a)
r2 = (- b - (d**0.5))//(2 * a)
print("the first root is:",r1)
print("the second root is:",r2)
