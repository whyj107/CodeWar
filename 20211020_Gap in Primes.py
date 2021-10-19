# Gap in Primes
# https://www.codewars.com/kata/561e9c843a2ef5a40c0000a4/train/python

# 나의 풀이
from collections import deque
def gap(g, m, n):
    p = deque()
    for i in range(m, n+1):
        if is_prime(i):
            if len(p) > 0:
                pre = p.pop()
                if i - pre == g:
                    return [pre, i]
            p.append(i)
    return None

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1))

# 다른 사람의 풀이
def gap1(g, m, n):
    previous_prime = n
    for i in range(m, n + 1):
        if is_prime(i):
            if i - previous_prime == g:
                return [previous_prime, i]
            previous_prime = i
    return None

print(gap(2, 100, 110), [101, 103])
print(gap(4, 100, 110), [103, 107])
print(gap(6, 100, 110), None)
print(gap(8, 300, 400), [359, 367])
print(gap(10, 300, 400), [337, 347])
print(gap(2, 100, 103), [101, 103])

