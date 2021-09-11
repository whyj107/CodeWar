# Floating-point Approximation (I)
# https://www.codewars.com/kata/58184387d14fc32f2b0012b2/train/python

# 나의 풀이
def f (x):
    return x / (1 + (1 + x)**0.5)

# 다른 사람의 풀이
def f1(x):
    return x / (1 + sqrt(1 + x))

def f2(x):
    return 1/2.0 * x - 1/8.0 * x ** 2 + 1/ 16.0 * x ** 3 - 5/128.0 * x **4

from math import sqrt, fabs
def assertFuzzyEquals(actual, expected, msg=""):
    merr = 1e-12
    if expected == 0:
        inrange = fabs(actual) <= merr
    else:
        e = fabs((actual - expected) / expected)
        inrange = e <= merr
    if msg == "":
        msg = "Expected value near {:.16e}, but got {:.16e}. Relative error: {:.16e}"
        msg = msg.format(expected, actual, e)
    return print(inrange, msg)

assertFuzzyEquals(f(2.6e-08), 1.29999999155e-08)
assertFuzzyEquals(f(1.4e-09), 6.999999997549999e-10)
assertFuzzyEquals(f(5.0e-06), 2.499996875007812e-06)
assertFuzzyEquals(f(2.4e-07), 1.1999999280000085e-07)

