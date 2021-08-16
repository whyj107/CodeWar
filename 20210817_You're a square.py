# You're a square!
# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

# 나의 풀이
def is_square(n):
    return int(n**0.5) == n**0.5 if n > -1 else False

# 다른 사람의 풀이
import math
def is_square1(n):
    return n > -1 and math.sqrt(n) % 1 == 0;

print(is_square(-1), False, "-1: Negative numbers cannot be square numbers")
print(is_square(0), True)
print(is_square(3), False)
print(is_square(4), True)
print(is_square(25), True)
print(is_square(26), False)
