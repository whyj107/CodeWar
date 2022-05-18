# Spinning Rings
# https://www.codewars.com/kata/59afff65f1c8274f270020f5/train/python

# 나의 풀이
def spinning_rings(inner_max, outer_max):
    cnt, inner, outer = 1, inner_max, 1
    while inner != outer:
        cnt += 1
        inner = inner_max if inner-1 < 0 else inner - 1
        outer = 0 if outer+1 > outer_max else outer + 1
    return cnt

# 다른 사람의 풀이
from itertools import count
def spinning_rings1(inner_max, outer_max):
    return next(i for i in count(1) if i % (outer_max + 1) == -i % (inner_max + 1))

def spinning_rings2(inner_max, outer_max):
    a, b, res = inner_max,1,1
    while a != b:
        a = (a + inner_max) % (inner_max+1)
        b = (b + 1) % (outer_max+1)
        res += 1
    return res

print(spinning_rings(2, 3), 5)
print(spinning_rings(3, 2), 2)
print(spinning_rings(1, 1), 1)
print(spinning_rings(2, 2), 3)
print(spinning_rings(3, 3), 2)