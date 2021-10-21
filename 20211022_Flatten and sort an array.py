# Flatten and sort an array
# https://www.codewars.com/kata/57ee99a16c8df7b02d00045f/train/python

# 나의 풀이
def flatten_and_sort(array):
    result = []
    for a in array:
        result += a
    return sorted(result)

# 다른 사람의 풀이
from itertools import chain
def flatten_and_sort1(array):
    return sorted((chain(*array)))

print(flatten_and_sort([]), [])
print(flatten_and_sort([[], []]), [])
print(flatten_and_sort([[], [1]]), [1])
print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(flatten_and_sort([[1, 3, 5], [100], [2, 4, 6]]), [1, 2, 3, 4, 5, 6, 100])