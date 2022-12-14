# Smallest possible sum
# https://www.codewars.com/kata/52f677797c461daaf7000740/train/python

# 나의 풀이
# TIMEOUT
def solution(a):
    l = len(a)
    if l < 2: return a[0]
    start = a[0]
    for i in range(l):
        tmp = step(a[i], start)
        if tmp == 1: return l
        start = tmp
    return tmp * l

def step(tmp, start):
    while tmp != start:
        if tmp > start:
            if tmp%start == 0: return start
            tmp %= start
        else:
            if start%tmp == 0: return tmp
            start %= tmp
    return tmp

# 다른 사람의 풀이
def solution1(a):
    a_len = len(a)
    a = set(a)
    while len(a) != 1:
        b = max(a)
        a.remove(b)
        a.add(b-max(a))
    return(max(a) * a_len)

from math import gcd
def solution2(a):
    return gcd(*a) * len(a)

print(solution([9]), 9)
print(solution([6, 9, 21]), 9)
print(solution([1, 21, 55]), 3)
print(solution([30, 12]), 12)
print(solution([1, 1, 1, 2]), 4)
