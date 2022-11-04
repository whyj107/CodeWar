# Fibofamily #1
# https://www.codewars.com/kata/635d422dfdfe6900283eb892/train/python

# 나의 풀이
"""
기본 피보나치 응용 버전 : 시간 초과
def G(n):
    x, y = 7, 31
    for i in range(n):
        x, y = y, (1+y)*(1+x)-1
    return x%9
"""

# 반복 된다 : 7 4 3 1 7 6 1 4 0 4 4 6 7 1 6 4 7 3 4 1 0 1 1 3
def G(n):
    r = [7, 4, 3, 1, 7, 6, 1, 4, 0, 4, 4, 6, 7, 1, 6, 4, 7, 3, 4, 1, 0, 1, 1, 3]
    return r[n%len(r)]

print(G(0), 7)
print(G(1), 4)
print(G(2), 3)
print(G(3), 1)
print(G(4), 7)
