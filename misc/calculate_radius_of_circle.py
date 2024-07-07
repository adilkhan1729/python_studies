import math

def calculate_fertizer(r):
    A = math.pi * (r**2)
    return A


print(calculate_fertizer(7))
radius = float(input("Please enter the radius"))
print(calculate_fertizer(radius))