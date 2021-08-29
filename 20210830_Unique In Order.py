# Unique In Order
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

# 나의 풀이
from itertools import groupby
def unique_in_order(iterable):
    return [list(g)[0] for _, g in groupby(iterable)]

# 다른 사람의 풀이
def unique_in_order1(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result

print(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])
