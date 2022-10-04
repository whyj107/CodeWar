# The Poet And The Pendulum
# https://www.codewars.com/kata/5bd776533a7e2720c40000e5/train/python

# 나의 풀이
def pendulum(values):
    result = []
    for idx, v in enumerate(sorted(values)):
        if idx % 2 == 0:
            result.insert(0, v)
        else:
            result.append(v)
    return result

# 다른 사람의 풀이
def pendulum1(a):
    a = sorted(a)
    return a[::2][::-1] + a[1::2]

from collections import deque
def pendulum2(values):
    x = deque()
    v = sorted(values)
    for i, n in enumerate(v):
        x.append(n) if i % 2 else x.appendleft(n)
    return list(x)

print(pendulum([4, 6, 8, 7, 5]), [8, 6, 4, 5, 7])
print(pendulum([19, 30, 16, 19, 28, 26, 28, 17, 21, 17]),
      [28, 26, 19, 17, 16, 17, 19, 21, 28, 30])
print(pendulum([-9, -2, -10, -6]),
      [-6, -10, -9, -2])
print(pendulum([-19, -9, -5, -6, -15, -16, -5, -12]),
      [-5, -9, -15, -19, -16, -12, -6, -5])
print(pendulum([11, -16, -18, 13, -11, -12, 3, 18]),
      [13, 3, -12, -18, -16, -11, 11, 18])