# Switch on the Gravity
# https://www.codewars.com/kata/64c743cb0a2a00002856ff73/train/python

# 나의 풀이
def switch_gravity(lst):
    r = []
    cnt = [i.count('#') for i in zip(*lst)]
    for i in cnt:
        tmp = ['-']*(len(lst)-i) + ['#']*i
        r.append(tmp)
    return [list(i) for i in zip(*r)]

# 다른 사람의 풀이
import numpy as np
def switch_gravity1(lst):
    return np.sort(lst, 0)[::-1].tolist()

def switch_gravity2(lst):
    return list(map(list, zip(*map(sorted, zip(*lst)))))[::-1]