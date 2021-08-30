# Common Denominators
# https://www.codewars.com/kata/54d7660d2daf68c619000d95/train/python

# 나의 풀이
def convert_fracts(lst):
    tmp = []
    lcm = 1
    for i, j in lst:
        g = gcd1(i, j)
        lcm = lcm*(j//g)//gcd1(lcm, j)
        tmp.append([i//g, j//g])
    return [[(lcm//j)*i, lcm] for i, j in tmp]
def gcd1(p, q):
    return gcd1(q, p%q) if q != 0 else p

# 다른 사람의 풀이
import math
import functools
def convertFracts1(lst):
    lcm = lambda a, b: abs(a*b) // math.gcd(a, b)
    tmp_list = list(map(lambda x: x[1], list(lst)))
    lcm_num = functools.reduce(lcm, tmp_list)
    return list(map(lambda x: [x[0] * lcm_num // x[1], lcm_num], list(lst)))

from functools import reduce
from fractions import gcd
def convertFracts2(lst):
    lcm = lambda x, y: x*y//gcd(x, y)
    D = reduce(lcm, (d for _, d in lst))
    return [[n*D//d, D] for n, d in lst]

a = []
b = []
print(convert_fracts(a), b)
a = [[1, 2], [1, 3], [1, 4]]
b = [[6, 12], [4, 12], [3, 12]]
print(convert_fracts(a), b)
a = [[2, 4], [2, 6], [2, 8]]
b = [[6, 12], [4, 12], [3, 12]]
print(convert_fracts(a), b)