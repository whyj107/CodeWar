# Steps in Primes
# https://www.codewars.com/kata/5613d06cee1e7da6d5000055/train/python

# 나의 풀이
def step(g, m, n):
    for i in range(m, n+1):
        if is_prime(i):
            if is_prime(i+g) and i+g <= n:
                return [i, i+g]
    return None

def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n ** 0.5)+1))

print(step(2, 100, 110), [101, 103])
print(step(4, 100, 110), [103, 107])
print(step(2, 5, 5), None)
print(step(6, 100, 110), [101, 107])
print(step(8, 300, 400), [359, 367])
print(step(10, 300, 400), [307, 317])