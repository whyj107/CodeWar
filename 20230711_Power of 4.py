# Power of 4
# https://www.codewars.com/kata/544d114f84e41094a9000439/train/python

# 나의 풀이
def powerof4(n):
    if type(n) != int: return False
    i = 0
    while 4**i < n:
        i += 1
    return True if 4**i == n else False

# 다른 사람의 풀이
from math import log
def powerof4_log(n):
    if type(n) in (float, int) and n > 0:
        return log(n,4).is_integer()
    return False