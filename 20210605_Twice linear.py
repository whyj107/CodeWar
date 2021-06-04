# Twice linear
# https://www.codewars.com/kata/5672682212c8ecf83e000050/train/python

# 나의 풀이
def dbl_linear(n):
    result = [1]
    y_idx, z_idx = 0, 0
    while len(result) <= n:
        y = 2*result[y_idx] + 1
        z = 3*result[z_idx] + 1
        if y > z:
            result.append(z)
            z_idx += 1
        elif y < z:
            result.append(y)
            y_idx += 1
        else:
            result.append(y)
            y_idx += 1
            z_idx += 1
    return result[n]

# 다른 사람의 풀이
from collections import deque
def dbl_linear1(n):
    u, q2, q3 = 1, deque([]), deque([])
    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if u == q2[0]: q2.popleft()
        if u == q3[0]: q3.popleft()
    return u

def dbl_linear2(n):
  num_list = [1]
  for i in num_list:
    num_list.append((i * 2) + 1)
    num_list.append((i * 3) + 1)
    if len(num_list) > n *10:
      break
  return sorted(list(set(num_list)))[n]

def dbl_linear3(n):
    u = [1]
    i = 0
    j = 0
    while len(u) <= n:
        x = 2 * u[i] + 1
        y = 3 * u[j] + 1
        if x <= y:
            i += 1
        if x >= y:
            j += 1
        u.append(min(x, y))
    return u[n]

print(dbl_linear(8), 19)
print(dbl_linear(10), 22)
print(dbl_linear(20), 57)
print(dbl_linear(30), 91)
print(dbl_linear(50), 175)
print(dbl_linear(500), 3355)
print(dbl_linear(1000), 8488)