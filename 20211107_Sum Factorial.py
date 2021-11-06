# Sum Factorial
# https://www.codewars.com/kata/56b0f6243196b9d42d000034/train/python

# 나의 풀이
def sum_factorial(lst):
    return sum(f(l) for l in lst)

def f(n):
    return None if n < 0 else (1 if n == 1 or n == 0 else n * f(n-1))

# 다른 사람의 풀이
def sum_factorial1(lst):
    return sum(map(fac1, lst)) if lst else None

def fac1(n):
    return n * fac1(n - 1) if n != 0 else 1

print(sum_factorial([4, 6]), 744)
print(sum_factorial([5, 4, 1]), 145)