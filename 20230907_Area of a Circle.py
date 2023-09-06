# Area of a Circle
# https://www.codewars.com/kata/537baa6f8f4b300b5900106c/train/python

# 나의 풀이
from math import pi
def circle_area(r):
    return False if type(r) != int or r < 1 else round(r*r*pi,2)

print(circle_area(2), 12.57, "Incorrect radius")
print(circle_area(-3), False, "Negative radii don't have circle areas")
print(circle_area('An Integer'), False, "Strings can't generate areas")
print(circle_area(0), False, "Radius of 0 can't generate an area")