# Sum Of Regular Numbers
# https://www.codewars.com/kata/58c20c8d61aefc518f0000fd/train/python

# 나의 풀이
def sum_of_regular_numbers(arr):
    tmp = {}
    idx = 0
    for a, b in zip(arr, arr[1:]):
        tmp.setdefault(b-a, [])
        if idx - 1 in tmp[b - a] or tmp[b - a] == []:
            tmp[b - a].append(idx)
        else:
            tmp[b - a] = [idx]
        idx += 1
    result = 0
    for k, v in tmp.items():
        if len(v) > 1:
            result += sum(arr[v[0]:v[-1]+2])
    return result

# 다른 사람의 풀이
from itertools import groupby, pairwise
def sum_of_regular_numbers1(numbers: list[int]) -> int:
    res = groupby(pairwise(numbers), key=lambda p: p[1] - p[0])
    res = (next(g) + tuple(p[1] for p in g) for _, g in res)
    return sum(sum(g) for g in res if len(g) >= 3)

print(sum_of_regular_numbers([54, 70, 86, 1, -2, -5, 0, 5, 78, 145, 212, 15]), 639)
print(sum_of_regular_numbers([59, 58, 57, 55, 53, 51]), 390)
print(sum_of_regular_numbers([7, 2, -3, 3, 9, 15]), 30)
print(sum_of_regular_numbers([-17, -9, 1, 9, 17, 4, -9]), 39)
print(sum_of_regular_numbers([7, 2, 3, 2, -2, 400, 802]), 1200)
print(sum_of_regular_numbers([-1, 7000, 1, -6998, -13997]), -13994)