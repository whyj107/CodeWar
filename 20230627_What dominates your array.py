# What dominates your array?
# https://www.codewars.com/kata/559e10e2e162b69f750000b4/train/python

# 나의 풀이
from collections import Counter
def dominator(arr):
    tmp = Counter(arr).most_common()
    if tmp == []: return -1
    if tmp[0][1] <= len(arr)/2: return -1
    return tmp[0][0]

# 다른 사람의 풀이
def dominator1(arr):
    for x in set(arr):
        if arr.count(x) > len(arr)/2.0:
            return x
    return -1

print(dominator([3, 4, 3, 2, 3, 1, 3, 3]), 3)
print(dominator([1, 2, 3, 4, 5]), -1)
print(dominator([1, 1, 1, 2, 2, 2]), -1)
print(dominator([1, 1, 1, 2, 2, 2, 2]), 2)
print(dominator([]), -1)
