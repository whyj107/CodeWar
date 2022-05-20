# Corner circle
# https://www.codewars.com/kata/5898761a9c700939ee000011/train/python

# 나의 풀이
# (r+x)^2 = 2*(r-x)2
# x = ...
from math import sqrt
def corner_circle(r):
    return round((sqrt(2)-1)*r/(1+sqrt(2)), 2)

# 다른 사람의 풀이
def corner_circle1(r):
    return round(r * 0.171572875, 2)

R = 2 ** 0.5 - 1
def corner_circle2(r):
    return round(r * R * R, 2)

print(corner_circle(3), 0.51)
print(corner_circle(17), 2.92)