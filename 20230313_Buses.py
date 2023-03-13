# Buses!
# https://www.codewars.com/kata/640dee7cbad3aa002e7c7de4/train/python

# 나의 풀이
from math import ceil

def buses(kids, adults, places):
    if places < 3 or (kids > 0 and adults < 2): return 0

    if kids + adults <= places: return 1

    a, b = divmod(kids, (places - 2))

    if (a + (0 if b == 0 else 1)) * 2 > adults: return 0

    if b == 0:
        cnt = a
        adults -= (a * 2)
    else:
        cnt = a + 1
        adults -= (a * 2 + places - b)
    cnt += (ceil(adults / places))
    return cnt

# 다른 사람의 풀이
import math
def buses1(k, a, p):
    if (a//2)*(p-2)<k:
        return 0
    else:
        return k//(p-2) + math.ceil((k%(p-2) + a-(k//(p-2))*2)/p)

# print(buses(10, 4, 5), 0)
print(buses(2, 4, 4), 2)
print(buses(23, 10, 38), 1)
print(buses(15, 45, 6), 10)

print(buses(1, 55, 3), 19)
print(buses(10, 4, 7), 2)
print(buses(4, 8, 3), 4)
print(buses(36, 33, 8), 9)
print(buses(2, 2, 7), 1)
print(buses(2, 2, 4), 1)
print(buses(6, 2, 9), 1)
