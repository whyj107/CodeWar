# Floating-point Approximation (III)
# https://www.codewars.com/kata/5b0c0ec907756ffcff00006e/train/python

# 풀이
def quadratic(a, b, c):
    return -c / b

def quadratic1(a, b, c):
    y = b * (1.0 - 2.0 * a * c / b / b)
    x1 = -(y + b) / (2 * a)
    x2 = c / (x1 * a)
    return x1 if abs(x1) < abs(x2) else x2

def quadratic2(a, b, c):
    y = b * (1.0 - 2.0 * a * c / b / b)
    # b > 0
    x1 = -(y + b) / (2 * a)
    x2 = c / (x1 * a)
    if abs(x1) < abs(x2):
        r = x1
    else:
        r = x2
    return r

from math import fabs
def assertFuzzyEquals(a, b, c, msg=""):
    # max error
    merr = 1e-12
    s = '{}, {:.2e}, {}'.format(a, b, c)
    print("Testing", s)
    x = quadratic(a, b, c)
    smallest = fabs(x) < 1.e-1
    if smallest == False:
        msg = "This root is not the good one"
        print(msg)
    actual = a * x * x + b * x + c
    print('Actual f(x) {:.12e}'.format(actual))
    inrange = fabs(actual) <= merr
    if inrange == False and msg == "":
        msg = "Expected value near {:.12e}, but got {:.12e}. Expected error <= {:.12e}"
        msg = msg.format(0, actual, merr)
        print(msg)
    correct = smallest and inrange
    print("Correct", correct)
    print("#")
    return print(correct, "root is not good")

def tests():
    assertFuzzyEquals(7, 4.00e+13, 8)
    assertFuzzyEquals(9, 1.00e+14, 1)
    assertFuzzyEquals(3, 3.00e+09, 1)
    assertFuzzyEquals(7, 4.00e+09, 7)
tests()
print("<COMPLETEDIN::>")
print("<COMPLETEDIN::>")

