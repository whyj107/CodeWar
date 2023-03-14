# Jumps in a cycle #1
# https://www.codewars.com/kata/63f844fee6be1f0017816ff1/train/python

# 나의 풀이
# 엄청 큰수는 통과 못했음... 결국 수식이 있다는 말임
def get_jumps0(cycle_list, k):
    cnt = 1
    i = 0
    while (i+k)%len(cycle_list) != 0:
        cnt += 1
        i += k
    return cnt


# 통과
from math import gcd
def get_jumps(cycle_list, k):
    l = len(cycle_list)
    tmp = gcd(l, k)
    return l//tmp

ex = ([1, 5, 7, 8, 9], 1)
print(get_jumps(*ex), 5)

ex = ([1, 5, 7, 8, 9], 2)
print(get_jumps(*ex), 5)

ex = ([1, 5, 1], 2)
print(get_jumps(*ex), 3)