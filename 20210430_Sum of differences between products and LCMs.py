# Sum of differences between products and LCMs
# https://www.codewars.com/kata/56e56756404bb1c950000992/train/python

# 나의 풀이
def sum_differences_between_products_and_LCMs(pairs):
    tmp1 = [a * b for a, b in pairs]
    tmp2 = [a*b//gcd(a, b) if a*b != 0 else 0 for a, b in pairs]
    return sum(a-b for a, b in zip(tmp1, tmp2))

def gcd(p, q):
    return p if q == 0 else gcd(q, p%q)

# 다른 사람의 풀이
from fractions import gcd

def sum_differences_between_products_and_LCMs1(pairs):
    return sum(a*b - a*b//gcd(a,b) for a, b in pairs if a and b)

print(sum_differences_between_products_and_LCMs([[15, 18], [4, 5], [12, 60]]), 840)
print(sum_differences_between_products_and_LCMs([[1, 1], [0, 0], [13, 91]]), 1092)
print(sum_differences_between_products_and_LCMs([[15, 7], [4, 5], [19, 60]]), 0)
print(sum_differences_between_products_and_LCMs([[20, 50], [10, 10], [50, 20]]), 1890)
print(sum_differences_between_products_and_LCMs([]), 0)