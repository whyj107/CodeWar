# Product Array(Array Series #5)
# https://www.codewars.com/kata/5a905c2157c562994900009d/train/python

# 나의 풀이
from functools import reduce
def product_array(numbers):
    pro = reduce((lambda x, y: x*y), numbers)
    return [pro//n for n in numbers]

# 다른 사람의 풀이
from operator import mul
def product_array1(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]

from numpy import prod
def product_array2(numbers):
    p = prod(numbers)
    return [p // i for i in numbers]

print(product_array([12, 20]), [20,12])
print(product_array([3, 27, 4, 2]), [216, 24, 162, 324])
print(product_array([13, 10, 5, 2, 9]), [900, 1170, 2340, 5850, 1300])
print(product_array([16, 17, 4, 3, 5, 2]), [2040, 1920, 8160, 10880, 6528, 16320])