# esreveR
# https://www.codewars.com/kata/5413759479ba273f8100003d/train/python

# 나의 풀이
def reverse(lst):
    result = [0]*len(lst)
    for idx, l in enumerate(lst):
        result[len(result)-idx-1] = l
    return result

# 다른 사람의 풀이
def reverse1(lst):
    out = list()
    for i in range(len(lst)-1,-1,-1):
        out.append(lst[i])
    return out

from collections import deque
def reverse2(lst):
    q = deque()
    for x in lst:
        q.appendleft(x)
    return list(q)

print(reverse(list([1, 2, 3])), [3, 2, 1])
print(reverse(list([1, None, 14, "two"])), ["two", 14, None, 1])
