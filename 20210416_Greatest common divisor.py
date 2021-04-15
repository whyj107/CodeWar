# Greatest common divisor
# https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd/train/python

# 나의 풀이
def mygcd(x, y):
    return mygcd(y, x % y) if y != 0 else x

# 다른 사람들의 풀이
def mygcd1(x,y):
    while y:
        x, y = y, x % y
    return x

import math
def mygcd2(x, y):
    return math.gcd(x, y)


print(mygcd(30, 12), 6)
print(mygcd(8, 9), 1)
print(mygcd(1, 1), 1)