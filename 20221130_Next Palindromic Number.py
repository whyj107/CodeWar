# Next Palindromic Number.
# https://www.codewars.com/kata/56a6ce697c05fb4667000029/train/python

# 나의 풀이
def next_pal(val):
    val += 1
    while str(val) != str(val)[::-1]:
        val += 1
    return val

# 다른 사람의 풀이
from itertools import count
def next_pal1(val):
    return next(c for c in count(val + 1) if str(c) == str(c)[::-1])

print(next_pal(11), 22)
print(next_pal(188), 191)
print(next_pal(191), 202)
print(next_pal(2541), 2552)