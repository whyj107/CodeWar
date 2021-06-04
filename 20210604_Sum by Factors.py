# Sum by Factors
# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/python

# 나의 풀이 : 시간 초과
def sum_for_list(lst):
    result = []
    for i in prime_range(max(lst)):
        tmp = [j//i for j in lst if j % i == 0]
        if tmp:
            result.append([i, sum(tmp) * i])
    return result

def prime_range(n):
    a = [False, False] + [True] * (n - 1)
    primes = []
    for i in range(2, n + 1):
        if a[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                a[j] = False
    return primes

# 다른 사람의 풀이 : 이것도 시간 초과
def sum_for_list2(lst):
    factors = {i for k in lst for i in range(2, abs(k)+1) if not k % i}
    prime_factors = {i for i in factors if not [j for j in factors-{i} if not i % j]}
    return [[p, sum(e for e in lst if not e % p)] for p in sorted(prime_factors)]

# 다른 사람의 풀이 : 정답
import math
def prime_factorisation(num):
    prime_factors = []
    num = abs(num)
    # Get number to be odd
    while num % 2 == 0:
        prime_factors.append(2)
        num = num / 2
    # Once we're down to an odd number, divide by 3, 5, 7, etc.
    for x in range(3, int(math.sqrt(num)) + 1, 2):
        while num % x == 0:
            prime_factors.append(x)
            num = num / x
    if num > 1:
        prime_factors.append(num)
    return prime_factors

def sum_for_list(lst):
    # Get prime factors
    prime_facs = set([])
    for x in lst:
        for fac in prime_factorisation(x):
            prime_facs.add(fac)
    prime_facs = list(prime_facs)
    prime_facs.sort()
    return [[p, sum([x for x in lst if x % p == 0])] for p in prime_facs]

a = [12, 15]
# print(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])

a = [15, 21, 24, 30, 45]
# print(sum_for_list(a), [[2, 54], [3, 135], [5, 90], [7, 21]])

a = [107, 158, 204, 100, 118, 123, 126, 110, 116, 100]
print(sum_for_list(a))
print([[2, 1032], [3, 453], [5, 310], [7, 126], [11, 110], [17, 204], [29, 116], [41, 123], [59, 118], [79, 158], [107, 107]])
