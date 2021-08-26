# Character with longest consecutive repetition
# https://www.codewars.com/kata/586d6cefbcc21eed7a001155/train/python

# 나의 풀이
from itertools import groupby
def longest_repetition(chars):
    result = [(_, len(tuple(g))) for _, g in groupby(chars)]
    result = sorted(result, key=lambda x: x[1], reverse=True)
    return result[0] if len(result) > 0 else ('', 0)

# 다른 사람의 풀이
def longest_repetition1(chars):
    max_char, max_count = '', 0
    char, count = '', 0
    for c in chars:
        if c != char:
            count, char = 0, c
        count += 1
        if count > max_count:
            max_char, max_count = char, count
    return max_char, max_count

def longest_repetition2(chars):
    from itertools import groupby
    return max(((char, len(list(group))) for char, group in groupby(chars)),
               key=lambda char_group: char_group[1], default=("", 0))

tests = [
    ["aaaabb", ('a', 4)],
    ["bbbaaabaaaa", ('a', 4)],
    ["cbdeuuu900", ('u', 3)],
    ["abbbbb", ('b', 5)],
    ["aabb", ('a', 2)],
    ["ba", ('b', 1)],
    ["", ('', 0)],
]

for inp, exp in tests:
    print(longest_repetition(inp), exp)