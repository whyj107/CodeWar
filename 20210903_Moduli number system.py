# Moduli number system
# https://www.codewars.com/kata/54db15b003e88a6a480000b9/train/python

# 나의 풀이
from functools import reduce
from math import gcd
def from_nb_2_str(n, modsys):
    result = [n%m for m in modsys]
    prod = reduce(lambda x, y: x*y, modsys)
    tmp = [gcd(i, j) for i, j in combinations(modsys, 2)]
    return f"-{'--'.join(map(str, result))}-" if prod > n and all(tmp) == 1 else "Not applicable"

# 다른 사람의 풀이
from itertools import combinations
# from fractions import gcd
def fromNb2Str1(n, modsys):
    if any(gcd(x, y) > 1 for x, y in combinations(modsys, 2)) or n > reduce(lambda x, y: x*y, modsys):
        return "Not applicable"
    return "-" + "--".join(str(n % m) for m in modsys) + "-"

print(from_nb_2_str(779, [8, 7, 5, 3]), "-3--2--4--2-")
print(from_nb_2_str(15, [8, 6, 5, 3]), "Not applicable")
print(from_nb_2_str(3450, [17, 5, 3]), "Not applicable")
print(from_nb_2_str(3450, [13, 11, 7, 5, 3, 2]), "-5--7--6--0--0--0-")
