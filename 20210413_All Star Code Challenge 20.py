# All Star Code Challenge #20
# https://www.codewars.com/kata/5865a75da5f19147370000c7/train/python

# 나의 풀이
def add_arrays(a, b):
    if len(a) != len(b): raise
    return [i+j for i, j in zip(a, b)]

# 다른 사람의 풀이
from operator import add
def solve(a, b):
    if len(a) != len(b): raise
    return list(map(add, a, b))

print(add_arrays([1, 2], [4, 5]), [5, 7])
print(solve(['a'], ['b']), ['ab'])
