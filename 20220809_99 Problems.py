# 99 Problems, #1: last in list
# https://www.codewars.com/kata/57d86d3d3c3f961278000005/train/python

# 나의 풀이
def last(lst):
    return lst[-1] if lst else None

# 다른 사람의 풀이
def last1(a):
    if a: return a[-1]

print(last([1, 2, 3]), 3)
print(last([]), None)