# Parameter Of Number
# https://www.codewars.com/kata/5902f1839b8e720287000028/train/python

# 나의 풀이
from math import lcm
from functools import reduce
def parameter(n):
    tmp = list(map(int, str(n)))
    return lcm(sum(tmp), reduce(lambda x,y:x*y, tmp))

# 다른 사람의 풀이
from math import gcd
def parameter1(n):
    s, p = 0, 1
    for m in str(n):
        s += int(m)
        p *= int(m)
    return (s * p / (gcd(s, p)))

sample_test_cases = [
    ('Small numbers', [
    #      n   expected
        (  22,    4),
        (1234,  120),
        (   1,    1),
        (   2,    2),
        (  11,    2),
        ( 239,  378),
        (  91,   90),
        ( 344,  528),
    ]),
    ('Large numbers', [
    #        n       expected
        (123456789,    362880),
        (999999999, 387420489),
    ]),
]

for name, test_cases in sample_test_cases:
    for n, expected in test_cases:
        print(parameter(n), expected, f'parameter({n})')