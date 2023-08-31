# Back and forth then Reverse!
# https://www.codewars.com/kata/60cc93db4ab0ae0026761232/train/python

# 나의 풀이
# 시간초과
def arrange(s):
    t = []
    while s != []:
        t.append(s.pop(0))
        if s != []:
            t.append(s.pop(-1))
        s = s[::-1]
    return t

# 풀이
from collections import deque

def arrange0(s):
    q=deque(s)
    return [q.pop() if 0<i%4<3 else q.popleft() for i in range(len(s))]

def arrange1(s):
    return [s[[i, -i, ~i, i][i % 4]//2] for i in range(len(s))]