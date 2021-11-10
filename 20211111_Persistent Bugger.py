# Persistent Bugger
# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

# 나의 풀이
from functools import reduce
def persistence(n):
    cnt = 0
    while n > 9:
        n = reduce(lambda x, y: x*y, list(map(int, str(n))))
        cnt += 1
    return cnt

# 다른 사람의 풀이
import operator
def persistence1(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i

print(persistence(39), 3)
print(persistence(4), 0)
print(persistence(25), 2)
print(persistence(999), 4)
