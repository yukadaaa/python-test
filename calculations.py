import math
#Кадочников Александр
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("на ноль не делится")
    return a / b

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def solve_quadratic(a, b, c):
    if a == 0:
        if b == 0:
            return None if c != 0 else (0,) 
        return (-c / b,)
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None 
    elif discriminant == 0:
        return (-b / (2 * a),) 
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)

def geometric_sum(a, r, n):
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)
