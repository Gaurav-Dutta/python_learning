a = int(input("Enter A: "))
if a == 0:
    print("'A' must be a nonzero number")
    quit()
b = int(input("Enter B: "))
c = int(input("Enter C: "))

import math
root1 = (-b + math.sqrt(b*b - 4*a*c))/ 2*a
root2 = (-b - math.sqrt(b*b - 4*a*c))/ 2*a

print(root1)
print(root2)