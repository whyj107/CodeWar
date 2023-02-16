# Decompose a number
# https://www.codewars.com/kata/55ec80d40d5de30631000025/train/python

# 나의 풀이
from math import log
def decompose(num):
    k = 2
    result = []

    while k < num:
        tmp = int(log(num, k))
        if tmp == 1: break;
        num -= pow(k, tmp)
        result.append(tmp)
        k += 1
    return [result, num]

# 다른 사람의 풀이
def decompose1(n):
    i = 2
    result = []
    while n >= i * i:
        k = int(log(n, i))
        result.append(k)
        n -= i ** k
        i += 1

    return [result, n]

print(decompose(0), [[], 0])
print(decompose(4), [[2], 0])
print(decompose(9), [[3], 1])
print(decompose(25), [[4, 2], 0])
print(decompose(8330475), [[22, 13, 10, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2], 0])
print(decompose(8331299), [[22, 13, 10, 8, 7, 6, 6, 5, 5, 5, 4, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2], 199])