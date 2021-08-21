# Backwards Read Primes
# https://www.codewars.com/kata/5539fecef69c483c5a000015/train/python

# 나의 풀이
def backwards_prime(start, stop):
    answer = []
    for i in range(start, stop+1):
        back = int(str(i)[::-1])
        if back != i:
            if isPrime(back) and isPrime(i):
                answer.append(i)
    return answer

def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def testing(n, m, exp):
    actual = backwards_prime(n, m)
    print(actual, exp)

# a1 = [7027, 7043, 7057]
# testing(7000, 7100, a1)

# a8 = []
# testing(400, 503, a8)

# a = [13, 17, 31, 37, 71, 73, 79, 97]
# testing(2, 100, a)

a = [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]
testing(70000, 70245, a)
