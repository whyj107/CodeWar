# Steps in k-primes
# https://www.codewars.com/kata/5a48948e145c46820b00002f/train/python

# 다른 사람의 풀이
def getK(n):
    p, nk = 2, 0
    while p < int(n ** 0.5 + 1):
        while not n % p:
            nk += 1
            n //= p
        p += 1 + (p != 2)
    return nk + (n != 1)

def kprimes_step(k, step, start, nd):
    return [[x, x+step] for x in range(start, nd-step+1) if getK(x) == k and getK(x+step) == k]

def testing(k, step, start, nd, expected):
    print(k, ",", step, ",", start, ",", nd, "\n")
    actual = kprimes_step(k, step, start, nd)
    print(actual, expected)

testing(10, 8, 2425364, 2425700, [])
testing(6, 8, 2627371, 2627581, [[2627408, 2627416], [2627440, 2627448], [2627496, 2627504]])