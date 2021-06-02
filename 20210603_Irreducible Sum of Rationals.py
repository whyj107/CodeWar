# Irreducible Sum of Rationals
# https://www.codewars.com/kata/5517fcb0236c8826940003c9/train/python

# 나의 풀이
from fractions import Fraction
def sum_fracts(lst):
    if lst == []: return None
    tmp = sum(Fraction(i, j) for i, j in lst)
    return tmp.numerator if tmp.denominator == 1 else [tmp.numerator, tmp.denominator]

# 다른 사람의 풀이
def sum_fracts1(lst):
    if lst:
        ret = sum(Fraction(a, b) for (a, b) in lst)
        return ret.numerator if ret.denominator == 1 else [ret.numerator, ret.denominator]

from operator import mul

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_fracts2(lst):
    d = reduce(mul, [frac[1] for frac in lst], 1)
    n = sum(frac[0] * d / frac[1] for frac in lst)
    gcd_dn = gcd(d, n)
    d = d / gcd_dn
    n = n / gcd_dn
    if lst:
        return int(n / d) if n % d == 0 else [n, d]
    else:
        return None

print(sum_fracts([[1, 2], [1, 3], [1, 4]]), [13, 12])
print(sum_fracts([[1, 3], [5, 3]]), 2)