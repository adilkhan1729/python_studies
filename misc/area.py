import math

def area(type):
    if type == 1:
        l = int(input("Please enter the length "))
        w = int(input("Please enter the width "))
        area = l*w
        return area
    elif type == 2:
        l = int(input("Please enter the length "))
        area = l*l
        return area
    elif type == 3:
        r = int(input("Please enter the radius "))
        area = math.pi * r *r
        return area
    
print("1. Choose 1 if you want to find the area of rectangle ")
print("2. Choose 2 if you want to find the area of square ")
print("3. Choose 3 if you want to find the area of circle ")
type = int(input("Please choose one of the below "))

print(area(type))
