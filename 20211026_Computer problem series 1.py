# Computer problem series #1: Fill the Hard Disk Drive
# https://www.codewars.com/kata/5d49c93d089c6e000ff8428c/train/python

# 나의 풀이
def save(sizes, hd):
    return sum(sum(sizes[:i])<=hd for i in range(1, len(sizes)+1))

# 다른 사람들의 풀이
from bisect import bisect
from itertools import accumulate
def save1(sizes, hd):
    return bisect(list(accumulate(sizes)), hd)

print(save([4, 4, 4, 3, 3], 12), 3)
print(save([4, 4, 4, 3, 3], 11), 2)
print(save([4, 8, 15, 16, 23, 42], 108), 6)
print(save([13], 13), 1)
print(save([1, 2, 3, 4], 250), 4)
print(save([100], 500), 1)
print(save([11, 13, 15, 17, 19], 8), 0)
print(save([45], 12), 0)