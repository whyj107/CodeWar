# Generating Numbers From Digits #1
# https://www.codewars.com/kata/584d05422609c8890f0000be/train/python

# 나의 풀이
import math
def proc_arr(arr):
    set_arr = set(arr)
    tmp = 1
    for i in set_arr:
        tmp *= math.factorial(arr.count(i))
    min_n = ''.join(sorted(arr))
    return [math.factorial(len(arr))//tmp, int(min_n), int(min_n[::-1])]

# 다른 사람의 풀이
"""
from operator import mul
from math import factorial
from functools import reduce
from collections import Counter

def proc_arr(arr):
    s = ''.join(sorted(arr))
    return [factorial(len(arr)) // reduce(mul, map(factorial, Counter(arr).values())), int(s), int(s[::-1])]

from collections import Counter
from math import factorial
def proc_arr(a):
    c, a = 1, ''.join(a)
    for i in Counter(a).values():
        c *= factorial(i)
    b = factorial(len(a)) // c
    return [b,int(''.join(sorted(a))),int(''.join(sorted(a)[::-1]))]
"""
print(proc_arr(['1','2','2','3','2','3']), [60, 122233, 332221])
print(proc_arr(['9', '9', '8', '8', '7', '4', '3', '2', '1', '1', '1']), [1663200, 11123478899, 99887432111])

arr = ['1', '2', '3', '0', '5', '1', '1', '3']
print(proc_arr(arr), [3360, 1112335, 53321110])

