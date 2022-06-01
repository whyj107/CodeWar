# Tortoise racing
# https://www.codewars.com/kata/55e2adece53b4cdcb900006c/train/python

# 나의 풀이
def race(v1, v2, g):
    if v1>v2 or (v1==v2 and g != 0): return None

    t = g/(v2-v1)
    h = int(t)
    m = int(t*60 - h*60)
    s = int(t*3600 - h*3600 - m*60)
    return [h, m, s]

# 다른 사람의 풀이
from datetime import datetime, timedelta
def race1(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        sec = timedelta(seconds=int((g * 3600 / (v2 - v1))))
        d = datetime(1, 1, 1) + sec

        return [d.hour, d.minute, d.second]

print(race(720, 850, 70), [0, 32, 18])
print(race(80, 91, 37), [3, 21, 49])
print(race(820, 81, 550), None)
