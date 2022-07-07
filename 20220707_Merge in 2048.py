# Merge in 2048
# https://www.codewars.com/kata/55e1990978c60e5052000011/train/python

# 나의 풀이
def merge(line):
    result = []
    pre = 0
    s = True
    for l in line:
        if l == 0: continue
        if pre == l and s:
            result[-1] += l
            s = False
        else:
            result.append(l)
            s = True
        pre = l
    return result + [0] * (len(line) - len(result))

# 다른 사람의 풀이
from itertools import groupby
def merge1(line):
    merged = []
    for k,g in groupby( v for v in line if v ):
        g = list(g)
        n,r = divmod(len(g),2)
        if n: merged.extend([k*2]*n)
        if r: merged.append(k)
    return merged + [0]*(len(line)-len(merged))

def merge2(line):
    lst = [x for x in line if x != 0]
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            lst = lst[:i] + [lst[i] + lst[i + 1]] + lst[i + 2:] + [0]
    return lst + [0] * (len(line) - len(lst))

print(merge([2, 0, 2, 2]), [4, 2, 0, 0])
print(merge([2, 0, 2, 4]), [4, 4, 0, 0])
print(merge([0, 0, 2, 2]), [4, 0, 0, 0])
print(merge([8, 16, 16, 8]), [8, 32, 8, 0])
print(merge([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0])
