# Primes in numbers
# https://www.codewars.com/kata/54d512e62a5e54c96200019e/train/python

# 나의 풀이
def prime_factors(n):
    result = ""
    for i in range(2, n+1):
        cnt = 0
        if i > n: break
        while n % i == 0:
            n //= i
            cnt += 1
        result += f"({i}**{cnt})" if cnt > 1 else (f"({i})" if cnt > 0 else "")
    return result

print(prime_factors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
print(prime_factors(86240), "(2**5)(5)(7**2)(11)")