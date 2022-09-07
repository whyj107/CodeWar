# Build a pile of Cubes
# https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

# 나의 풀이
# 1^3 + 2^3 + ... + (n-1)^3 + n^3 = m
# (n*(n+1)/2)^2 = m
# n^2 + n - 2*sqrt(m) = 0
# 근의 공식 사용
from math import sqrt
def find_nb(m):
    n = int((-1+sqrt(1+8*sqrt(m)))/2)
    return n if sum([pow(i, 3) for i in range(n+1)]) == m else -1

# 다른 사람의 풀이
def find_nb1(m):
    n = 1
    volume = 0
    while volume < m:
        volume += n**3
        if volume == m:
            return n
        n += 1
    return -1

from math import floor
def find_nb2(m):
    n_canidate = int(floor(sqrt(2 * sqrt(m))))
    if (n_canidate * (n_canidate + 1) / 2)**2 == m:
        return n_canidate
    else:
        return -1
print(find_nb(4183059834009), 2022)
print(find_nb(24723578342962), -1)
print(find_nb(135440716410000), 4824)
print(find_nb(40539911473216), 3568)
print(find_nb(26825883955641), 3218)
print(find_nb(10252519345963644753026), -1)
print(find_nb(1512059869225966097), -1)
