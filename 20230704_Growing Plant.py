# Simple Fun #74: Growing Plant
# https://www.codewars.com/kata/58941fec8afa3618c9000184/train/python

# 나의 풀이
def growing_plant(up, ds, dh):
    if up >= dh: return 1
    tmp = 0
    r = 0
    while tmp < dh:
        r += 1
        tmp += up
        if tmp >= dh: break
        tmp -= ds
    return r

# 다른 사람의 풀이
def growing_plant1(upSpeed, downSpeed, desiredHeight):
    days = 1
    height = upSpeed
    while (height < desiredHeight):
        height += upSpeed - downSpeed
        days += 1
    return days

from math import ceil
def growing_plant2(up, down, h):
    return max(ceil((h - down) / (up - down)), 1)