# Find the Maximum Length of a Chain
# https://www.codewars.com/kata/64b779a194167920ebfbdd2e/train/python

# 풀이
def len_longest_chain0(pairs):
    pairs = sorted(pairs)
    s = pairs[-1][1] + 1
    n = 0
    for i, j in reversed(pairs):
        if j < s:
            n += 1
            s = i
    return n

# 신기한거
from operator import itemgetter
def len_longest_chain(pairs):
    res, x = 0, float('-inf')
    for a, b in sorted(pairs, key=itemgetter(1)):
        print(x, a, b, res)
        if x < a:
            res, x = res+1, b
    return res

print(len_longest_chain([(2, 3), (3, 4), (3, 5)]), 1)
"""
print(len_longest_chain([(2, 3), (3, 4), (1, 2)]), 2)
print(len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]), 4)
print(len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]), 3)
"""