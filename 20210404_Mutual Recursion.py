# Mutual Recursion
# https://www.codewars.com/kata/53a1eac7e0afd3ad3300008b/train/python
# kata 6

# 나의 풀이
def f(n):
    if n == 0: return 1
    return n - m(f(n-1))

def m(n):
    if n == 0: return 0
    return n - f(m(n-1))

# 다른 사람의 풀이
def f1(n): return n - m1(f1(n-1)) if n else 1

def m1(n): return n - f1(m1(n-1)) if n else 0

print(f(0), 1)
print(f(5), 3)
print(f(10), 6)
print(m(0), 0)
print(m(5), 3)
print(m(10), 6)
