# Prime Factors
# https://www.codewars.com/kata/542f3d5fd002f86efc00081a/train/python

# 나의 풀이
def prime_factors(n):
    result = []
    p = 2
    while n!=1:
        if n%p == 0:
            result.append(p)
            n //= p
        else:
            p += 1
    return result

# 다른 사람의 풀이
def prime_factors1(n):
    a, b = 2, []
    while n>1:
        while not n%a:
            b += [a]
            n = n//a
        a += 1
    return b

print(prime_factors(1), [])
print(prime_factors(3), [3])
print(prime_factors(8), [2, 2, 2])
print(prime_factors(9), [3, 3])
print(prime_factors(12), [2, 2, 3])