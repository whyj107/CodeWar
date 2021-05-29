# Robinson Crusoe
# https://www.codewars.com/kata/5d95b7644a336600271f52ba/train/python

# 풀이
from math import cos, sin, radians
def crusoe(n, d, ang, dist_mult, ang_mult):
    x, y, a = 0, 0, radians(ang)
    for i in range(n):
        x += d * cos(a)
        y += d * sin(a)
        d *= dist_mult
        a *= ang_mult
    return x, y

def assert_fuzzy(n, d, ang, distmult, angmult, expect):
    # max error
    merr = 1e-12
    actual = crusoe(n, d, ang, distmult, angmult)
    e1 = abs(actual[0] - expect[0])
    e2 = abs(actual[1] - expect[1])
    inrange = e1 <= merr and e2 <= merr
    msg = "Expected value near ({:.12e}, {:.12e}), got ({:.12e}, {:.12e})"
    msg = msg.format(expect[0], expect[1], actual[0], actual[1])
    print(msg)
    return print(inrange, "Error")

print(assert_fuzzy(8, 0.22, 3, 1.01, 1.15, (1.814652098870, 0.164646220964)))
print(assert_fuzzy(29, 0.13, 21, 1.01, 1.09, (0.318341393410, 2.292862212314)))
print(assert_fuzzy(45, 0.10, 3, 1.01, 1.10, (2.689897523779, 2.477953232467)))
print(assert_fuzzy(14, 0.22, 20, 1.02, 1.14, (1.774076472485, 2.557008479031)))
print(assert_fuzzy(42, 0.11, 17, 1.02, 1.09, (0.528555980656, 2.196434600133)))