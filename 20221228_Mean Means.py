# Mean Means
# https://www.codewars.com/kata/57c6b44f58da9ea6c20003da/train/python

# 나의 풀이
from functools import reduce
def geo_mean(nums, arith_mean):
    l = len(nums)+1
    nums.append(arith_mean*l-sum(nums))
    return reduce(lambda x, y: x*y, nums)**(1/l)

# 다른 사람의 풀이
from operator import mul
def geo_mean1(nums, mean):
    nums.append(mean*(len(nums)+1)-sum(nums))
    return reduce(mul, nums) ** (1/len(nums))

from math import prod
def geo_mean2(nums, arith_mean):
    nums.append(arith_mean * (len(nums)+1) - sum(nums))
    return prod(nums)**(1/len(nums))

print(geo_mean([2], 10), 6)
print(geo_mean([1, 2], 3), 2.2894284851066637)
print(geo_mean([4, 6, 7, 2], 5), 4.580344097847165)