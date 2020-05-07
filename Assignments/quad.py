import math
def get_roots(a, b, c):
    root1 = (-b + math.sqrt(b*b - 4*a*c))/ 2*a
    root2 = (-b - math.sqrt(b*b - 4*a*c))/ 2*a
    return([root1, root2])
