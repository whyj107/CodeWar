# Numbers that are a power of their sum of digits
# https://www.codewars.com/kata/55f4e56315a375c1ed000159/train/python

# 나의 풀이
# TIME OUT
from math import log
def power_sumDigTerm(n):
    result = []
    cnt = 81
    while len(result) < n:
        x = sum([int(j) for j in str(cnt)])
        try:
            tmp = log(cnt, x)
            if pow(x, round(tmp)) == cnt:
                result.append(cnt)
        except:
            pass
        cnt += 1
    return result[n-1]

# 다른 사람의 풀이 : 단순하게 하는게 빨랐다니...
def power_sumDigTerm1(n):
    r = []
    for i in range(2, 1000):
        for k in range(2, 40):
            c = i**k
            tmp = sum(int(d) for d in str(c))**k
            if c == tmp:
                r.append(c)
    r.sort()
    return r[n-1]

for n, expected in [(1, 81), (2, 512), (3, 2401), (4, 4913), (5, 5832)]:
    print(power_sumDigTerm(n), expected) 
"""
for i in range(81, 513):
    solve(i)
"""