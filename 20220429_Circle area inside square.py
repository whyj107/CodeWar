# Circle area inside square
# https://www.codewars.com/kata/5899aa695401a83a5c0000c4/train/python

# 나의 풀이
from math import pi
def square_area_to_circle(size):
    return size/4*pi


print(round(square_area_to_circle(9), 8), round(7.0685834705770345, 8))
print(round(square_area_to_circle(20), 8), round(15.70796326794897, 8))