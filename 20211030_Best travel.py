# Best travel
# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

# 나의 풀이
from itertools import combinations
def choose_best_sum(t, k, ls):
    l = [sum(i) for i in combinations(ls, k) if sum(i) <= t]
    return max(l) if l else None

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
print(choose_best_sum(230, 4, xs), 230)
print(choose_best_sum(430, 5, xs), 430)
print(choose_best_sum(430, 8, xs), None)
