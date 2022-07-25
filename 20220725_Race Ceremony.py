# Race Ceremony
# https://www.codewars.com/kata/62cecd4e5487c10028996e04/train/python

# 나의 풀이
import math
def race_podium(blocks):
    a, b, c = round(blocks/3), math.ceil(blocks/3), blocks//3
    if a == b:
        c -= 1
        b += 1
    if a == c:
        if c != 2:
            c -= 2
            a += 1
        else:
            c -= 1
        b += 1
    return (a, b, c)

# 다른 사람의 풀이
from math import ceil
def race_podium1(b):
    f = ceil((b) / 3) + 1
    s = min(f - 1, b - f - 1)
    return s, f, b - f - s

print(race_podium(11), (4, 5, 2))
print(race_podium(6), (2, 3, 1))
print(race_podium(10), (4, 5, 1))
print(race_podium(100000), (33334, 33335, 33331))
print(race_podium(7), (2, 4, 1))
print(race_podium(8), (3, 4, 1))
