# Are the numbers in order?
# https://www.codewars.com/kata/56b7f2f3f18876033f000307/train/python

# 나의 풀이
def in_asc_order(arr):
    return arr == sorted(arr)

# 다른 사람의 풀이
def in_asc_order1(a):
    return all(x < y for x, y in zip(a, a[1:]))

in_asc_order2 = lambda l: sorted(l) == l