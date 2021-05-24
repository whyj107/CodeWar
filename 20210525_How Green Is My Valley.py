# How Green Is My Valley?
# https://www.codewars.com/kata/56e3cd1d93c3d940e50006a4/train/python

# 나의 풀이
from collections import deque
def make_valley(arr):
    tmp = deque([])
    left = False
    if len(arr) % 2 != 0: left = True
    for idx, i in enumerate(sorted(arr)):
        if left:
            tmp.appendleft(i)
            left = False
        else:
            tmp.append(i)
            left = True
    return list(tmp)

# 다른 사람의 풀이
def make_valley1(arr):
    arr = sorted(arr, reverse=True)
    return arr[::2] + arr[1::2][::-1]

def testing(actual, expected):
    print(actual, expected)

testing(make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]), [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17])
testing(make_valley([20, 7, 6, 2]), [20, 6, 2, 7])
testing(make_valley([14, 10, 8]), [14, 8, 10])
testing(make_valley([20, 18, 17, 13, 12, 12, 10, 9, 4, 2, 2, 1, 1]), [20, 17, 12, 10, 4, 2, 1, 1, 2, 9, 12, 13, 18])
testing(make_valley([20, 16, 14, 10, 1]), [20, 14, 1, 10, 16])
testing(make_valley([19, 19, 18, 14, 12, 11, 9, 7, 4]), [19, 18, 12, 9, 4, 7, 11, 14, 19])
testing(make_valley([20, 18, 16, 15, 14, 14, 13, 13, 10, 9, 4, 4, 4, 1]), [20, 16, 14, 13, 10, 4, 4, 1, 4, 9, 13, 14, 15, 18])
testing(make_valley([20, 20, 16, 14, 12, 12, 11, 10, 3, 2]), [20, 16, 12, 11, 3, 2, 10, 12, 14, 20])
testing(make_valley([19, 17, 16, 15, 13, 8, 5, 5, 4, 4, 4]), [19, 16, 13, 5, 4, 4, 4, 5, 8, 15, 17])
testing(make_valley([19, 8, 6]), [19, 6, 8])