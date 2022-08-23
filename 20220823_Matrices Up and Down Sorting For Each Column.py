#8 Matrices: Up and Down Sorting For Each Column
# https://www.codewars.com/kata/590b8d5cee471472f40000aa/train/python

# 나의 풀이
def up_down_col_sort(matrix):
    i, arrow = 0, 1
    result = [[] for _ in matrix]
    tmp = sorted([m for ma in matrix for m in ma])
    for t in tmp:
        result[i].append(t)
        i += arrow
        if i == len(result) or i < 0:
            arrow *= -1
            i += arrow
    return result

# 다른 사람의 풀이
from itertools import chain, cycle
def up_down_col_sort1(matrix):
    direction = cycle([1, -1])
    n = len(matrix)
    xs = sorted(chain.from_iterable(matrix))
    xss = [xs[i:i+n][::next(direction)] for i in range(0, len(xs), n)]
    return map(list, zip(*xss))

M = [[-20, -4, -1],
     [1, 4, 7],
     [8, 10, 12]]

print(up_down_col_sort(M),
      [[-20, 7, 8], [-4, 4, 10], [-1, 1, 12]])

M2 = [[1, -1, 4, 1],
      [7, -20, 12, 0],
      [8, 10, -4, -3]]
print(up_down_col_sort(M2),
      [[-20, 1, 1, 12], [-4, 0, 4, 10], [-3, -1, 7, 8]])

M3 = [[1, -1, 4, 1],
      [7, -20, 12, 0],
      [8, 10, -4, -3],
      [5, 6, 6, 8]]
print(up_down_col_sort(M3), [[-20, 4, 5, 12], [-4, 1, 6, 10], [-3, 1, 6, 8], [-1, 0, 7, 8]])