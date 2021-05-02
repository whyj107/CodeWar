# Factorial
# https://www.codewars.com/kata/57a049e253ba33ac5e000212/train/python

# 나의 풀이
def factorial0(n):
    return 1 if n == 0 else n * factorial(n-1)

# 다른 사람의 풀이
from math import factorial

tests = (
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
)

for t in tests:
    inp, exp = t
    print(factorial(inp), exp)