# Smallest Product
# https://www.codewars.com/kata/5b6b128783d648c4c4000129/train/python

# 나의 풀이
from functools import reduce
def smallest_product(a):
    return min([reduce((lambda x, y: x*y), i) for i in a])

# 다른 사람의 풀이
from math import prod
def smallest_product1(a):
    return min(map(prod, a))

print(smallest_product([[3, 2], [1, 2, 1], [7, 8]]), 2)
print(smallest_product([[10], [3, 0], [-1, -6, 2]]), 0)