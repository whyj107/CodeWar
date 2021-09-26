# (a+b)^n
# https://www.codewars.com/kata/61419e8f0d12db000792d21a/train/python

# 나의 풀이
def formula(n):
    tmp = []
    if n == 0: return str(1)
    for i in range(0, abs(n)+1):
        x = solve(abs(n), i)
        x = "" if x == 1 else str(x)
        a = f'a^{abs(n)-i}' if (abs(n)-i) > 1 else ('a' if (abs(n)-i) == 1 else "")
        b = f'b^{i}' if i > 1 else ('b' if i == 1 else "")
        tmp.append(str(x) + a + b)
    return f'1/({"+".join(tmp)})' if n < 0 else '+'.join(tmp)

from math import factorial
def solve(n, r):
    return factorial(n)//(factorial(n-r)*factorial(r))

# ===================================================================================
# 다른 사람의 풀이
from math import comb
def formula1(n):
    return (f'1/({formula(-n)})' if n < 0 else '1' if not n else
    '+'.join(binom(n - i, i) for i in range(n + 1)))
def binom(a, b):
    c = comb(a + b, a)
    return f"{c if c > 1 else ''}{term('a', a)}{term('b', b)}"
def term(c, n):
    return f'{c}^{n}' if n > 1 else c if n else ''

# print(formula(0), "1")
print(formula(1), "a+b")
print(formula(2), "a^2+2ab+b^2")
print(formula(3), "a^3+3a^2b+3ab^2+b^3")
print(formula(5), "a^5+5a^4b+10a^3b^2+10a^2b^3+5ab^4+b^5")
print(formula(-1), "1/(a+b)")
print(formula(-2), "1/(a^2+2ab+b^2)")
print(formula(-4), "1/(a^4+4a^3b+6a^2b^2+4ab^3+b^4)")