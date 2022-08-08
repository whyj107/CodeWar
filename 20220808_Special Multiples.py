# Special Multiples
# https://www.codewars.com/kata/55e785dfcb59864f200000d9/train/python

# 나의 풀이
def count_specMult(n, max_val):
    tmp_n = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    tmp_r = 1
    for i in range(n):
        tmp_r *= tmp_n[i]
    return max_val//tmp_r

# 다른 사람의 풀이
from functools import reduce
from operator import mul
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
def count_specMult1(n, limit):
    return (limit - 1) // reduce(mul, PRIMES[:n])
print(count_specMult(3, 200), 6)
print(count_specMult(3, 1000), 33)
print(count_specMult(4, 500), 2)
print(count_specMult(4, 1000), 4)