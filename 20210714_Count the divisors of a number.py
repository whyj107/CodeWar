# Count the divisors of a number
# https://www.codewars.com/kata/542c0f198e077084c0000c2e/train/python

# 나의 풀이
def divisors(n):
    result = [0]*(n+1)
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result[i] = 1
            if i**2 != n:
                result[n//i] = 1
    return sum(result)

# 다른 사람의 풀이
# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors1 = lambda n: sum([n % x == 0 for x in range(1, n + 1)])

print(divisors(1), 1)
print(divisors(4), 3)
print(divisors(5), 2)
print(divisors(12), 6)
print(divisors(30), 8)
print(divisors(4096), 13)