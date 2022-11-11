# Padovan numbers
# https://www.codewars.com/kata/5803ee0ed5438edcc9000087/train/python

# 나의 풀이
# 재귀 형식 | TimeOut
def padovan0(n):
    if n < 3: return 1
    return padovan0(n-2) + padovan0(n-3)

def padovan(n):
    x, y, z = 1, 1, 1
    for i in range(n):
        x, y, z = y, z, x+y
    return x

# 다른 사람의 풀이
from functools import lru_cache
@lru_cache(maxsize=None)
def padovan1(n):
    return n<3 or padovan1(n-2) + padovan1(n-3)

tests = [ # [input, expected]
    [0, 1],
    [1, 1],
    [2, 1],
    [3, 2],
    [4, 2],
    [5, 3],
    [6, 4],
    [7, 5],
    [8, 7],
    [9, 9]
]

for inp, exp in tests:
    print(padovan(inp), exp)