# Deodorant Evaporator
# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/python

# 문제를 이해 못했다. 설명을 너무 조금 줬던 문제.
# 풀이
def evaporator(content, evap_per_day, threshold):
    n = 0
    current = 100
    percent = 1 - evap_per_day / 100.0
    while current > threshold:
        current *= percent
        n += 1
    return n

import math
def evaporator1(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold / 100.0) / math.log(1.0 - evap_per_day / 100.0))

print(evaporator(10, 10, 10), 22)