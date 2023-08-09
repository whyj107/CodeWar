# Coprimes up to N
# https://www.codewars.com/kata/59e0dbb72a7acc3610000017/train/python

# 나의 풀이
from math import gcd
def coprimes(n):
    return [i for i in range(1, n+1) if gcd(i, n)==1]

# 다른 사람의 풀이
from fractions import gcd
def coprimes1(n):
  return [i for i in range(1,n+1) if gcd(n,i)==1]

print(coprimes(2), [1])
print(coprimes(3), [1, 2])
print(coprimes(6), [1, 5])
print(coprimes(10), [1, 3, 7, 9])
print(coprimes(20), [1, 3, 7, 9, 11, 13, 17, 19])
print(coprimes(25), [1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24])
print(coprimes(30), [1, 7, 11, 13, 17, 19, 23, 29])