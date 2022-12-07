# Pure odd digits primes
# https://www.codewars.com/kata/55e0a2af50adf50699000126/train/python

# 나의 풀이
# [
# n 미만의 순수 홀수 소수의 갯수,
# n보다 작은 최대 순수 홀수 소수,
# n보다 큰 순수 최소 홀수 소수
# ]
def only_oddDigPrimes (n):
    odd_primes = [i for i in range(n+1) if is_pureOdd(i) if is_prime(i)]
    while not(is_prime(n) and is_pureOdd(n)):
        n += 1
    return [len(odd_primes), odd_primes[-1], n]

def is_prime(n):
    return n > 1 and all(n%i !=0 for i in range(2, int(n**0.5)+1))

def is_pureOdd(n):
    return n > 2 and all(i not in ['2', '4', '6', '8', '0'] for i in str(n))

print(only_oddDigPrimes(20), [7, 19, 31])
print(only_oddDigPrimes(40), [9, 37, 53])
print(only_oddDigPrimes(55), [10, 53, 59])
print(only_oddDigPrimes(60), [11, 59, 71])