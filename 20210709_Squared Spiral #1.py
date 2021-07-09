# Squared Spiral #1
# https://www.codewars.com/kata/60a38f4df61065004fd7b4a7/train/python

# 나의 풀이
import math
def squared_spiral(n):
    if n == 0: return (0, 0)
    idx = round(n**0.5)
    start = math.ceil(idx / 2)
    n_ = -1
    if idx % 2 == 0:
        start *= -1
        n_ = 1
    tmp = idx**2 + idx - n
    if tmp < idx:
        return (start, start+n_*tmp)
    else:
        return (start+n_*(tmp-idx), start+n_*idx)

# 다른 사람의 풀이
def squared_spiral1(n):
    b = round(n**.5)
    e = (b//2+b%2-max(0, b**2-n), -(b//2) + max(0, n-b**2))
    return e if b % 2 else (-e[0], -e[1])

# print(squared_spiral(0), (0, 0))
# print(squared_spiral(6), (-1, -1))
# print(squared_spiral(10), (2, 0))
# print(squared_spiral(12), (2, 2))
# print(squared_spiral(30), (3, 3))
# print(squared_spiral(50264), (-112, 24))
# print(squared_spiral(50263), (-112, 25))
print(squared_spiral(25155), (-46, -79))