# Reverse sublists of even numbers
# https://www.codewars.com/kata/64c7bbad0a2a00198657013d/train/python

# 나의 풀이
def rev_sub(arr):
    r = []
    even = []
    for a in arr:
        if a%2 == 0:
            even.append(a)
        else:
            r += even[::-1]
            even = []
            r.append(a)
    r += even[::-1]
    return r

# 다른 사람의 풀이
from itertools import groupby
def rev_sub1(arr):
    r = []
    for i in [list(g) for n,g in groupby(arr, key = lambda x : x%2)]:
        if i[0]%2:
            r += i
        else:
            r += i[::-1]
    return r
