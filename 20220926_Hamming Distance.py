# Hamming Distance - Part 1: Binary codes
# https://www.codewars.com/kata/5624e574ec6034c3a20000e6/train/python

# 나의 풀이
def hamming_distance(a, b):
    return sum([1 for i, j in zip(a, b) if i != j])

# 다른 사람의 풀이
def hamming_distance1(a, b):
    return sum(c != d for c, d in zip(a, b))

from operator import ne
def hamming_distance2(a: str, b: str) -> int:
    return sum(map(ne, a, b))

print(hamming_distance('100101', '101001'), 2)
print(hamming_distance('1010', '0101'), 4)
print(hamming_distance('100101011011010010010', '101100010110010110101'), 9)