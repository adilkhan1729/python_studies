import math

def getArea(shape, l, w = -1):
    if shape == "rect" and w == -1: #Its a square
        return l*l
    elif shape == "rect":
        return l * w
    elif shape == "circle":
        return math.pi * l * l
    elif shape == "triangle":
        return 0.5 * w *l