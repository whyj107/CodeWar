# Can you sum?
# https://www.codewars.com/kata/638bc5d372d41880c7a99edc/train/python

# 나의 풀이
# TIME OUT
def f0(n:int) -> int:
    result = 0
    m = 10**9 + 7
    for i in range(n+1):
        result += (2**i) * (i**2)
    return result % m

# 다른 사람의 풀이
M = 10**9 + 7
def f(n:int) -> int:
    # g(x) = sum(x^k, k = 0..n)
    # Then sum(k^2 * x^2, k = 0..n) = x^2 g''(x) + x(g'(x) - 1) + x
    # g'(2) = (n - 1) * 2^n + 1
    # g''(2) = ...
    g2 = lambda n: (n * n * pow(2, n, M) - 3 * n * pow(2, n, M) + pow(2, n + 2, M) - 4) * pow(2, M - 2, M)
    g1 = lambda n: pow(2, n, M) * (n - 1) + 1
    return (4 * g2(n) + 2 * (g1(n) - 1) + 2) % M
    # Wolfram Alpha:
    return 2 * (pow(2, n, M) * (n * n - 2 * n + 3) - 3) % M

m = 1000000007
def f1(n: int) -> int:
    return (pow(2, n + 1, m) * (n * (n - 2) + 3) - 6) % m

"""
print(f(3), 90)
print(f(420), 118277878)
print(f(666), 483052609)
print(f(1111111111111), 284194637)
"""
