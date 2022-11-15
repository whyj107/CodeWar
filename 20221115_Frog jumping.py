# Frog jumping
# https://www.codewars.com/kata/536950ffc8a5ca9982001371/train/python

# 나의 풀이
def solution(a):
    cnt, index = 0, 0
    while cnt <= len(a):
        cnt += 1
        index += a[index]
        if index >= len(a) or index < 0:
            return cnt
    return -1

# 다른 사람의 풀이
def solution1(a):
    if not a: return -1
    posSet, i = set(), 0
    while i not in posSet:
        posSet.add(i)
        i += a[i]
        if not (0 <= i < len(a)):
            return len(posSet)
    return -1

print(solution([1, 2, 2, -1]), 4)
print(solution([1, 2, 1, 5]), 3)
print(solution([1, -1]), -1)
print(solution([-3, 4, 4, 0, -1, -2, 5, 3, -3, 5, 6, 0, -1, 1, 3, 1, 0, 7, -3, -1, -2]), 1)