# Looking for a benefactor
# https://www.codewars.com/kata/569b5cec755dd3534d00000f/train/python

# 문제를 이해하기 어려운 문제
from math import ceil
def new_avg(arr, newavg):
    value = int(ceil((len(arr) + 1) * newavg - sum(arr)))
    if value < 0:
        raise ValueError
    return value

def new_avg1(arr, newavg):
    extra = newavg*float(len(arr) + 1) - sum(arr)
    if extra < 0:
        raise ValueError
    return int(extra + 0.999)

print(new_avg([14, 30, 5, 7, 9, 11, 16], 90), 628)
print(new_avg([14, 30, 5, 7, 9, 11, 15], 92), 645)