# Highest number with two prime factors
# https://www.codewars.com/kata/55f347cfb44b879e1e00000d/train/python

# 풀이 : 모르겠음!
# 수학식으로 푸는 법
from math import log, ceil
def highest_biPrimefac (p1, p2, n):
    max_p1 = ceil(log(n/p2, p1))
    max_p2 = ceil(log(n/p1, p2))
    return max(([p1**x*p2**y, x, y] for x in range(1, max_p1) for y in range(1, max_p2)), key=lambda z:(z[0]<=n, z[0]))

# while로 푸는 법
def highest_biPrimefac2 (p1, p2, n): # p1, p2 primes and p1 < p2
    factors = {}
    k1, k2 = 1, 1
    while p1 ** k1 * p2 ** k2 <= n:
        while p1 ** k1 * p2 ** (k2 + 1) <= n:
            k2 += 1
        factors[p1 ** k1 * p2 ** k2] = (k1, k2)
        k1, k2 = k1 + 1, 1
    m = max(factors)
    return [m, factors[m][0], factors[m][1]]

print(highest_biPrimefac(2, 3, 50), [48, 4, 1])
print(highest_biPrimefac(5, 11, 1000), [605, 1, 2])
print(highest_biPrimefac(3, 13, 5000), [4563, 3, 2])
print(highest_biPrimefac(5, 7, 5000), [4375, 4, 1])