# Integers: Recreation Two
# https://www.codewars.com/kata/55e86e212fce2aae75000060/train/python

# n = e^2 + f^2

# 잘모르겠어서 다른 사람 풀이로 공부함
def prod2sum(a, b, c, d):
    e = sorted([abs(a*d-b*c), abs(a*c+b*d)])
    f = sorted([abs(a*c-b*d), abs(a*d+b*c)])
    return [e] if e == f else sorted([e, f])

print(prod2sum(1, 2, 1, 3), [[1, 7], [5, 5]])
print(prod2sum(2, 3, 4, 5), [[2, 23], [7, 22]])
print(prod2sum(1, 2, 2, 3), [[1, 8], [4, 7]])
print(prod2sum(1, 1, 3, 5), [[2, 8]])
