# Rotate for a Max
# https://www.codewars.com/kata/56a4872cbb65f3a610000026/train/python

# 나의 풀이
from collections import deque
def max_rot(n):
    result, i = [n], ''
    n = deque(str(n))
    while n:
        n.rotate(-1)
        i += str(n.popleft())
        result.append(int(i+''.join(n)))
    return max(result)

# 다른 사람의 풀이
def max_rot1(n):
    s, arr = str(n), [n]
    for i in range(len(s)):
        s = s[:i] + s[i+1:] + s[i]
        arr.append(int(s))
    return max(arr)

print(max_rot(38458215), 85821534)
print(max_rot(195881031), 988103115)
print(max_rot(896219342), 962193428)
print(max_rot(69418307), 94183076)
print(max_rot(507992495), 507992495)