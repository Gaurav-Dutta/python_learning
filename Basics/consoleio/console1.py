#the print and input function allow you to read and write from the console
#these two functions allows for basic user interactivity with a program

import math
def calculate_circumference(r):
    x = 2*math.pi*r
    return x

rad = float(input("enter radius: "))
c = calculate_circumference(rad)
print(c)
