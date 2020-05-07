import math

def calculate_hypotenuse (a, b):
    x = a*a + b*b
    return math.sqrt(x)

#print(calculate_hypotenuse(2, 2))

def calculate_area_circle (r):
    return math.pi*math.pow(r, 2)

#print(calculate_area_circle(3))