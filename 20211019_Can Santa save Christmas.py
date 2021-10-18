# Can Santa save Christmas?
# https://www.codewars.com/kata/5857e8bb9948644aa1000246/train/python

# 나의 풀이
from datetime import timedelta
def determine_time(arr):
    result = timedelta()
    for a in arr:
        a = a.split(":")
        result += timedelta(hours=int(a[0]), minutes=int(a[1]), seconds=int(a[2]))
    return result <= timedelta(1)

# 다른 사람의 풀이
def determine_time1(arr):
    total = 0

    for time in arr:
        h, m, s = map(int, time.split(":"))
        total += h * 60 * 60 + m * 60 + s

    return total <= 24 * 60 * 60

import pandas as pd
def determine_time(arr):
    SEC = 86400  # seconds per day
    return pd.Series(pd.to_timedelta(arr)).dt.total_seconds().sum() <= SEC

print(determine_time(["01:00:00", "02:30:00"]), True)
print(determine_time(["01:00:00", "02:30:00", "22:00:00"]), False)
print(determine_time(["12:00:00", "12:00:00"]), True)
print(determine_time([]), True)