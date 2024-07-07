import math

def perimeter(l,shape,w=-1):
    if shape=="circle" and w==-1:     
        return 2*math.pi*l
    elif shape=="rect":
        return 2*l+2*w
    elif shape=="sqaure" and w==-1:
        return 4*l
  

