# The dropWhile Function
# https://www.codewars.com/kata/54f9c37106098647f400080a/train/python

# My Solution
def drop_while(arr, pred):
    for idx, a in enumerate(arr):
        if pred(a):
            return arr[idx:]
    return []

# 다른 사람의 풀이
from itertools import dropwhile
def drop_while1(arr, pred):
    return list(dropwhile(pred, arr))

is_even=lambda n: not n%2
is_odd=lambda n: n%2

print(drop_while([2, 6, 4, 10, 1, 5, 4, 3], is_even), [1, 5, 4, 3])
print(drop_while([2, 100, 1000, 10000, 10000, 5, 3, 4, 6], is_even), [5, 3, 4, 6])
print(drop_while([998, 996, 12, -1000, 200, 0, 1, 1, 1], is_even), [1, 1, 1])
print(drop_while([1, 4, 2, 3, 5, 4, 5, 6, 7], is_even), [1, 4, 2, 3, 5, 4, 5, 6, 7])
print(drop_while([2, 4, 10, 100, 64, 78, 92], is_even), [])
print(drop_while([1, 2, 3, 4, 5], is_odd), [2, 3, 4, 5])
print(drop_while([1, 5, 111, 1111, 1111, 2, 4, 6, 4, 5], is_odd), [2, 4, 6, 4, 5])
print(drop_while([-1, -5, 127, 86, 902, 2, 1], is_odd), [86, 902, 2, 1])
print(drop_while([2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0], is_odd), [2, 1, 2, 4, 3, 5, 4, 6, 7, 8, 9, 0])
print(drop_while([1, 3, 5, 7, 9, 111], is_odd), [])