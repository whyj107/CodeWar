# Simple Fun #142: Mobius function
# https://www.codewars.com/kata/58aa5d32c9eb04d90b000107/train/python

# 나의 풀이
# TIME OVER----------------------------
def mobinus0(n):
    f = factorization(n)
    return 0 if max(f.values()) > 1 else (-1)**len(f)
def factorization(n):
    a, result = 2, {}
    while n>1:
        while not n%a:
            if not a in result.keys():
                result[a] = 1
            else:
                result[a] += 1
                return result
            n //= a
        a += 1
    return result
# -------------------------------------

def mobius(n):
    d = divisors(n)
    for i in d:
        if i**2 in d:
            return 0
    return (-1)**(sum([is_prime(i) for i in d]))

def divisors(n):
    result = set()
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            result.add(i)
            result.add(n//i)
    return sorted(result) + [n]

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

# 다른 사람의 풀이
def mobius2(n):
    sP, p = set(), 2
    while n>1 and p <= n**.5:
        while not n%p:
            if p in sP: return 0
            sP.add(p)
            n //= p
        p += 1 + (p!=2)
    return (-1)**((len(sP) + (n!= 1)) % 2)

# original----------------------------------
def divisors_original(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            result.add(i)
            result.add(n//i)
    return sorted(result)

def factorization_original(n):
    a, result = 2, []
    while n>1:
        while not n%a:
            result += [a]
            n = n//a
        a += 1
    return result
# ------------------------------------------


print(mobius(10), 1)
print(mobius(9), 0)
print(mobius(8), 0)
print(mobius(100000000001), 0)
print(mobius(7), -1)
print(mobius(5), -1)
print(mobius(30), -1)

print(mobius(pow(10, 12)-3), 1)