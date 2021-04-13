# All Star Code Challenge #24
# https://www.codewars.com/kata/5866c6cf442e3f16f9000089/train/python

# 나의 풀이
def hypotenuse(a, b):
    return (a**2+b**2)**0.5

def leg(c, a):
    return (c**2-a**2)**0.5

# 다른 사람의 풀이
import math

def hypotenuse(a, b):
    return math.hypot(a, b)

def leg(c, a):
    return math.sqrt(c**2-a**2)

print(hypotenuse(4, 3), 5)
print(leg(5, 3), 4)