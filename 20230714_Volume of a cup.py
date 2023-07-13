# Volume of a cup
# https://www.codewars.com/kata/56a13035eb55c8436a000041/train/python

# 원뿔대의 부피 구하기
# 나의 풀이
from math import pi
def cup_volume(d1, d2, h):
    d1, d2 = d1/2, d2/2
    return round(1/3*pi*h*(d1*d1+d1*d2+d2*d2), 2)

# 다른 사람의 풀이
def cup_volume2(d1, d2, h):
    return round(h / 12.0 * pi * (d1**2 + d1*d2 + d2**2), 2)

print(cup_volume(1, 1, 1), 0.79)
print(cup_volume(10, 8, 10), 638.79)
print(cup_volume(1000, 1000, 1000), 785398163.4)
print(cup_volume(13.123, 123.12, 1), 4436.57)
print(cup_volume(5, 12, 31), 1858.51)