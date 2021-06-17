# Bonuses
# https://www.codewars.com/kata/5d68d05e7a60ba002b0053f6/train/python

# 나의 풀이 : 시간 초과
def bonus0(arr, s):
    tmp = list(arr[0]/a for a in arr)
    return list(round(a*s/sum(tmp)) for a in tmp)

# 다른 사람의 풀이
def bonus(arr, s):
    s = s/(sum(1/n for n in arr))
    return [round(s/n) for n in arr]


def dotest(arr, s, expect):
    actual = bonus(arr, s)
    print(actual == expect)

dotest([22, 3, 15], 18228, [1860, 13640, 2728])
dotest([8, 14, 11], 23541, [10241, 5852, 7448])
dotest([8, 20, 17], 25281, [13515, 5406, 6360])
dotest([25, 22, 15, 22, 22], 5213, [858, 975, 1430, 975, 975])
dotest([10, 11, 30, 12, 17, 23, 30, 11, 17, 10], 1788210,
       [258060, 234600, 86020, 215050, 151800, 112200, 86020, 234600, 151800, 258060])