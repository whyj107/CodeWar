# Factorial
# https://www.codewars.com/kata/54ff0d1f355cfd20e60001fc/train/python

# 나의 풀이
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

import math
def factorial1(n):
    if n<0 or n>12:
        raise ValueError
    return math.factorial(n)

# 다른 사람의 풀이
def factorial(n):
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n*factorial(n-1)

print(factorial(0), 1)
print(factorial(1), 1)
print(factorial(2), 2)
print(factorial(3), 6)