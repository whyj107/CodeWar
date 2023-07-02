# Triangle type
# https://www.codewars.com/kata/53907ac3cd51b69f790006c5/train/python

# 나의 풀이
# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
    big = max(a, b, c)
    sma = min(a, b, c)
    mi = a + b + c - big - sma
    tmp = sma + mi
    if big >= tmp: return 0
    elif big**2 == (sma**2 + mi**2): return 2
    elif big**2 > (sma**2 + mi**2): return 3
    else: return 1

# 다른 사람의 풀이
def triangle_type1(a, b, c):
    x, y, z = sorted([a, b, c])
    if z >= x + y: return 0
    if z * z == x * x + y * y: return 2
    return 1 if z * z < x * x + y * y else 3

print(triangle_type(7,3,2), 0) # Not triangle
print(triangle_type(2,4,6), 0) # Not triangle
print(triangle_type(8,5,7), 1) # Acute
print(triangle_type(3,4,5), 2) # Right
print(triangle_type(7,12,8), 3) # Obtuse
