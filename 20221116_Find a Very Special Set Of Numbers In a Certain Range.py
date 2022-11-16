# Find a Very Special Set Of Numbers In a Certain Range
# https://www.codewars.com/kata/569df0bc5565b243d500002b/train/python

# 나의 풀이
from math import lcm
def find_us(n1, n2, k, prime_factors, digits):
    result = []
    lcm_n = 1
    for p in prime_factors:
        lcm_n = lcm(p, lcm_n)

    for i in range(n1 - n1 % lcm_n, n1 + k * n2, lcm_n):
        if i % lcm_n != 0: continue
        if all([str(d) in str(i) for d in digits]):
            result.append(i)
    return result

# 다른 사람의 풀이
# from math import lcm
def find_us1(n1, n2, k, prime_factors, digits):
    step, digits, end = 1, ''.join(map(str, digits)), 1 + n1 + k * n2

    for p in prime_factors:
        step = lcm(step, p)
    while n1 % step:
        n1 += 1
    return [i for i in range(n1, end, step) if all(j in str(i) for j in digits)]


from functools import reduce
from operator import mul
from math import ceil
def find_us2(n1, n2, k, prime_factors, digits):
    p = reduce(mul, prime_factors)
    d = set(map(str, digits))
    return [x for x in range(ceil(n1/p)*p, n1+k*n2+1, p) if d <= set(str(x))]

print(find_us(30, 90, 4, [2, 3], [6, 2]),
      [126, 162, 216, 246, 264, 276])
print(find_us(30, 400, 18, [2, 3, 7], [6, 2, 5]),
      [2562, 2856, 5628, 6258, 6552])

# print(find_us(500, 8000, 2500, [2, 3], [6, 2]))