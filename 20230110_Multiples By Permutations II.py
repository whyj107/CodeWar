# Multiples By Permutations II
# https://www.codewars.com/kata/5ba178be875de960a6000187/train/python

# 나의 풀이
from collections import Counter
def find_lowest_int(k):
    k1 = k+1
    n = 1
    while Counter(str(k1*n)) != Counter(str(k*n)):
        n += 1
    return n

# 다른 사람의 풀이
from itertools import count
def find_lowest_int1(k):
    return next(n for n in count(1) if sorted(str(n*k)) == sorted(str(n*(k+1))))

print(find_lowest_int(325), 477)
print(find_lowest_int(599), 2394)
print(find_lowest_int(855), 999)
print(find_lowest_int(1), 125874)
print(find_lowest_int(100), 8919)
print(find_lowest_int(1000), 89919)
print(find_lowest_int(10000), 899919)