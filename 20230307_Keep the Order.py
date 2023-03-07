# Keep the Order
# https://www.codewars.com/kata/582aafca2d44a4a4560000e7/train/python

# 나의 풀이
def keep_order(ary, val):
    result = 0
    for _ in ary:
        if _ < val:
            result += 1
    return result

# 다른 사람의 풀이
# bisect : 2진 탐색을 쉽게 구현하게끔 해주는 함수
from bisect import bisect_left
def keep_order1(arr, val):
    return bisect_left(arr, val)

print(keep_order([1, 2, 3, 4, 7], 5), 4)
print(keep_order([1, 2, 3, 4, 7], 0), 0)
print(keep_order([1, 1, 2, 2, 2], 2), 2)
print(keep_order([1, 2, 3, 4], 5), 4)
print(keep_order([1, 2, 3, 4], -1), 0)
print(keep_order([1, 2, 3, 4], 2), 1)
print(keep_order([1, 2, 3, 4], 0), 0)
print(keep_order([1, 2, 3, 4], 1), 0)
print(keep_order([1, 2, 3, 4], 2), 1)
print(keep_order([1, 2, 3, 4], 3), 2)
