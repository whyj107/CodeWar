# Sum of Intervals
# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

# 나의 풀이
def sum_of_intervals(intervals):
    intervals = sorted(set(intervals))
    pre = (-1000000000, -1000000000)
    result = 0
    for start, end in intervals:
        if start < pre[1] and end < pre[1]:
            continue
        elif start < pre[1]:
            result += (end-start-(pre[1]-start))
        else:
            result += (end-start)
        pre = (start, end)
    return result

# 다른 사람의 풀이
def sum_of_intervals1(intervals):
    s, top = 0, float("-inf")
    for a, b in sorted(intervals):
        if top < a:
            top = a
        if top < b:
            s, top = s+b-top, b
    return s

"""
print(sum_of_intervals([(1, 5)]), 4)
print(sum_of_intervals([(1, 5), (6, 10)]), 8)
print(sum_of_intervals([(1, 5), (1, 5)]), 4)
print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)
"""
print(sum_of_intervals([(-263, 72), (-260, 351), (-193, -165), (-189, 456), (-82, 235), (-25, -10), (-24, 93), (67, 248), (236, 293), (287, 464), (311, 445), (416, 481), (427, 480), (452, 475), (470, 474), (492, 494)]),
      746)