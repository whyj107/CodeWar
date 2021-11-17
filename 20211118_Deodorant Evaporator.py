# Deodorant Evaporator
# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f/train/python

# 나의 풀이
def evaporator(content, evap_per_day, threshold):
    tmp, result = 1, 0
    while tmp >= (threshold/100):
        tmp -= (tmp * (evap_per_day / 100))
        result += 1
    return result

# 다른 사람의 풀이
import math
def evaporator1(content, evap_per_day, threshold):
    return math.ceil(math.log(threshold / 100.0) / math.log(1.0 - evap_per_day / 100.0))

print(evaporator(10, 10, 10), 22)
print(evaporator(10, 10, 5), 29)