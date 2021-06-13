# Heron's formula
# https://www.codewars.com/kata/57aa218e72292d98d500240f/train/python

# 나의 풀이
import math
def heron(a, b, c):
    return round(math.sqrt((a+b+c)*(b+c-a)*(a+c-b)*(a+b-c)/16), 3)

# 다른 사람의 풀이
def heron1(a, b, c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 2)

print(heron(3, 4, 5), 6)