# Rotate Array
# https://www.codewars.com/kata/5469e0798a3502f4a90005c9/train/python

# 나의 풀이
from collections import deque
def rotate(data, n):
    data = deque(data)
    data.rotate(n)
    return list(data)

# 다른 사람의 풀이
def rotate1(data, n):
    if data:
        x = -n%len(data)
        return data[x:] + data[:x]
    return []

print(rotate([1, 2, 3, 4, 5], 1), [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], -1), [2, 3, 4, 5, 1])
print(rotate([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], -2), [3, 4, 5, 1, 2])
print(rotate([1, 2, 3, 4, 5], 3), [3, 4, 5, 1, 2])
print(rotate([1, 2, 3, 4, 5], -3), [4, 5, 1, 2, 3])
print(rotate([1, 2, 3, 4, 5], 4), [2, 3, 4, 5, 1])
print(rotate([1, 2, 3, 4, 5], -4), [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
print(rotate([1, 2, 3, 4, 5], -5), [1, 2, 3, 4, 5])
print(rotate([1, 2, 3, 4, 5], 6), [5, 1, 2, 3, 4])
print(rotate([1, 2, 3, 4, 5], -6), [2, 3, 4, 5, 1])
print(rotate([True, True, False], 2), [True, False, True])
print(rotate([1, 2, 3, 4, 5], 12478), [3, 4, 5, 1, 2])
print(rotate([], 976999), [])
