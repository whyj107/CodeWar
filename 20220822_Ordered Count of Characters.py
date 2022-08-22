# Ordered Count of Characters
# https://www.codewars.com/kata/57a6633153ba33189e000074/train/python

# 나의 풀이
from collections import Counter
def ordered_count(inp):
    tmp = Counter(inp)
    return [(i, tmp[i]) for i in tmp]

# 다른 사람의 풀이
def ordered_count1(input):
    return list(Counter(input).items())

tests = (
    ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
    ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)])
)

for t in tests:
    inp, exp = t
    print(ordered_count(inp), exp)