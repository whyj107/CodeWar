# Simple Fun #112: Array Erasing
# https://www.codewars.com/kata/589d1c08cc2e997caf0000e5/train/python

# 도저히 어떻게 풀어야하는지 감이 안와서 다른 사람의 풀이로 공부!!
# 다른 사람의 풀이
from itertools import groupby
def array_erasing(arr):
    a = [len(tuple(g)) for _,g in groupby(arr)]
    n = 1
    while len(a) > 1:
        i = max(range(len(a)), key=lambda i: (a[i]>1, -abs(i-len(a)//2)))
        a[max(0,i-1):i+2] = [sum(a[max(0,i-1):i+2])-a[i]]
        n += 1
    return n

def array_erasing1(lst):
    arr = [(1 - 2 * x) * len(tuple(g)) for x, g in groupby(lst)]

    def plucked(arr, i):
        if i == 0:            return arr[1:]
        if i == len(arr) - 1: return arr[:-1]
        return arr[:i - 1] + [arr[i - 1] + arr[i + 1]] + arr[i + 2:]

    count = 0
    while len(arr) > 2:
        i = len(arr) // 2
        if abs(arr[i]) > 1:
            arr = plucked(arr, i)
        else:
            k = 1
            while k < i:
                if abs(arr[i - k]) > 1:
                    arr = plucked(arr, i - k)
                    break
                elif abs(arr[i + k]) > 1:
                    arr = plucked(arr, i + k)
                    break
                k += 1
            if i == k:
                if abs(arr[0]) > 1:
                    arr = plucked(arr, 0)
                elif abs(arr[-1]) > 1:
                    arr = plucked(arr, len(arr) - 1)
                else:
                    arr = plucked(arr, i)
        count += 1
    return count + len(arr)

import re
def rem(l):
    m = len(l) // 2
    s = [m]
    for i in range(1, len(l)):
        if m + i < len(l):
            s.append(m + i)
        if m - i > -1:
            s.append(m - i)
    print(s, l)
    for i in [1, 0]:
        for j in s:
            if len(l[j]) > i:
                l.pop(j)
                return l
    return l

def array_erasing2(lst):
    c = 0
    while lst:
        l = ''.join(list(map(str, lst)))
        o = re.findall('0+|1+', l)
        if len(o) == 2:
            return c + len(set(o))
        lst = rem(o)
        c += 1
    return c

def array_erasing3(lst):
    if lst==[1, 0, 1, 0, 1, 0, 0, 1]:return 5
    if lst==[0, 0, 0, 1, 0, 0]:return 3
    if lst==[1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1]:return 6
    oc=0 if lst[0]==0 else 1
    zc=0 if lst[0]==1 else 1
    bef=lst[0]
    for i in range(1,len(lst)):
        if bef!=lst[i]:
            if lst[i]==1:oc+=1
            else:zc+=1
        bef=lst[i]
    if lst.count(1)==1:return max(oc,zc)+1
    if lst.count(0)==1:return max(oc,zc)+1
    if oc<zc:
        return oc+1
    return zc+1

for input, expected in [
    # ([0, 1, 1, 1, 0],                               2),
    # ([0, 1],                                        2),
    ([1, 0, 1, 0],                                  3),
    ([1, 1, 0, 0, 1, 1, 0],                         3),
    ([0, 0, 1, 0, 0, 1, 1, 0, 0],                   3),
    ([1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1], 3),
    ([0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],          3),
    ([1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],    3),
    ([1, 0, 1, 0, 1, 0, 0, 1],                      5),
    ([0, 0, 0, 1, 0, 0],                            3),
    ([1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],    6),]:
    print(array_erasing(input), expected)
