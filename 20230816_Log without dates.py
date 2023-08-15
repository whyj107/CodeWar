# Log without dates
# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6/train/python

# 나의 풀이
import datetime
def check_logs(log):
    cnt = 0
    pre = datetime.timedelta(hours=0, minutes=0, seconds=0)
    for idx, i in enumerate(log):
        i = list(map(int, i.split(":")))
        i = datetime.timedelta(hours=i[0], minutes=i[1], seconds=i[2])
        if pre >= i or idx == 0:
            cnt += 1
        pre = i
    return cnt

# 다른 사람의 풀이
check_logs1 = lambda log: sum(a >= b for a, b in zip(log, log[1:])) + bool(log)

from itertools import pairwise, starmap
from operator import ge
def check_logs2(ages):
    return bool(ages) + sum(starmap(ge, pairwise(ages)))