# Add All
# https://www.codewars.com/kata/5b7d7ce57a0c9d86c700014b/train/python

# 풀이 : 이거 못 푼 문제
def add_all(lst):
    if len(lst) == 1: return 0

    lst.sort()
    cost = sum(lst[:2])
    lst[:2] = cost,

    return cost + add_all(lst)

from heapq import *
def add_all1(lst):
    heapify(lst)
    total = 0
    while len(lst) > 1:
        s = heappop(lst) + heappop(lst)
        total += s
        heappush(lst, s)

    return total

print(add_all([1, 2, 3]), 9)
print(add_all([1, 2, 3, 4]), 19)
print(add_all([1, 2, 3, 4, 5]), 33)