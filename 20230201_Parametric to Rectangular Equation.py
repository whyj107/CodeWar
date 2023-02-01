# Parametric to Rectangular Equation
# https://www.codewars.com/kata/5b13530f828fab68820000c4/train/python

# 나의 풀이
import re
from math import lcm
def para_to_rect(eqn1, eqn2):
    pattern = "(-?t|-?\d+)"
    x = re.findall(pattern, eqn1.replace(' ', ''))
    y = re.findall(pattern, eqn2.replace(' ', ''))

    x[0] = x[0].replace('t', '1')
    y[0] = y[0].replace('t', '1')

    xa = -1 * int(x[0][1:]) if '-' in x[0] else int(x[0])
    ya = -1 * int(y[0][1:]) if '-' in y[0] else int(y[0])

    xb = -1 * int(x[-1][1:]) if '-' in x[-1] else int(x[-1])
    yb = -1 * int(y[-1][1:]) if '-' in y[-1] else int(y[-1])

    l = lcm(xa, ya)

    xa, ya = l//xa, l//ya

    if xa < 0:
        xa *= -1
        ya *= -1
    ya *= -1

    _ = '-' if ya < 0 else '+'
    xa_tmp = '-' if xa == -1 else ('' if xa == 1 else xa)
    ya_tmp = '' if abs(ya) == 1 else abs(ya)

    return f'{xa_tmp}x {_} {ya_tmp}y = {xa*xb + ya*yb}'

# 다른 사람의 풀이
from math import gcd
def para_to_rect1(eqn1, eqn2):
    a, b = eqn1.split('= ')[1].split('t ')
    c, d = eqn2.split('= ')[1].split('t ')
    if a in ("", "-"): a += '1'
    if c in ("", "-"): c += '1'
    a, b, c, d = map(eval, (a, b, c, d))
    x = gcd(a, c)
    e, f = c//x, -a//x
    if e < 0: e, f = -e, -f
    return f"{e if e>1 else ''}x {'+-'[f<0]} {abs(f) if abs(f)>1 else ''}y = {e*b + f*d}"

def para_to_rect2(eqn1, eqn2):
    to_int = lambda x: 1 if not x else -1 if x == '-' else int(x)
    coefs = lambda eq: map(to_int, re.search(r'(-?\d*)t([-+]\d+)', eq.replace(' ', '')).group(1, 2))
    (a, b), (c, d) = coefs(eqn1), coefs(eqn2)
    x, y, z = c, -a, c * b - a * d
    g = gcd(x, y, z)
    x //= g; y //= g; z //= g
    if x < 0:
        x, y, z = -x, -y, -z
    return f'{"" if x == 1 else x}x {"+-"[y < 0]} {"" if abs(y) == 1 else abs(y)}y = {z}'


print(1, para_to_rect('x = 12t + 18', 'y = 8t + 7'), '2x - 3y = 15')
print(2, para_to_rect('x = -12t + 18', 'y = 8t + 7'), '2x + 3y = 57')
print(3, para_to_rect('x = 12t + 18', 'y = -8t + 7'), '2x + 3y = 57')
print(4, para_to_rect('x = -12t + 18', 'y = -8t + 7'), '2x - 3y = 15')
print(5, para_to_rect("x = -t + 12", "y = 12t - 1"), "12x + y = 143")
print(5, para_to_rect("x = t + 1", "y = -t - 1"), "x + y = 0")
