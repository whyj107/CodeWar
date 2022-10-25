# Nth Smallest Element (Array Series #4)
# https://www.codewars.com/kata/5a512f6a80eba857280000fc/train/python

# 나의 풀이
def nth_smallest(arr, pos):
    return sorted(arr)[pos-1]

# 다른 사람의 풀이
from heapq import nsmallest
def nth_smallest1(arr, pos):
    return nsmallest(pos, arr)[-1]

print(nth_smallest([3, 1, 2], 2), 2)
print(nth_smallest([15, 20, 7, 10, 4, 3], 3), 7)
print(nth_smallest([-5, -1, -6, -18], 4), -1)
print(nth_smallest([-102, -16, -1, -2, -367, -9], 5), -2)
print(nth_smallest([2, 169, 13, -5, 0, -1], 4), 2)
