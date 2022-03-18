# Tertration
# https://www.codewars.com/kata/5797bbb34be9127074000132/train/python

# 4^0
# 7^1
# 2^(2^2) 이런 식으로 계산

# 나의 풀이
def tetration(x, y):
    if y == 0: return 1
    elif y == 1: return x
    else:
        result = x
        for _ in range(y-1):
            result = pow(x, result)
        return result

# 다른 사람의 풀이
from functools import reduce
from itertools import repeat

def tetration1(x, y):
    return reduce(int.__rpow__, repeat(x, y), 1)

def tetration2(x, y):
    result = 1
    for _ in range(y):
        result = pow(x, result)
    return result


print(tetration(4, 0), 1)
print(tetration(7, 1), 7)
print(tetration(5, 2), 3125)
print(tetration(2, 3), 16)