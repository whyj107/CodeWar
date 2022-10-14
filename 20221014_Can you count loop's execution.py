# Can you count loop's execution?
# https://www.codewars.com/kata/633bbba75882f6004f9dae4c/train/python

# 다른 사람의 풀이
def count_loop_iterations(arr):
    result = []
    acc = 1
    for n, b in arr:
        n = n + 2 if b else n + 1
        result.append(acc * n)
        acc *= n - 1
    return result

import math
def count_loop_iterations1(arr):
    arr = [i+j for i,j in arr]
    return [math.prod(arr[0:idx]) * (i+1) for idx, i in enumerate(arr)]

print(count_loop_iterations([(4, True), (5, False), (3, True)]), [6, 30, 125])
print(count_loop_iterations([(16, False), (11, False), (1, True), (3, False), (8, True), (10, True), (9, False), (11, True), (20, True), (3, False), (7, False)]), [17, 192, 528, 1408, 10560, 114048, 1045440, 12231648, 248396544, 948423168, 5690539008])
print(count_loop_iterations([]), [])
print(count_loop_iterations([(20, False)]), [21])
