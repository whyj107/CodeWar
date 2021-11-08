# Experimenting with a sequence of complex numbers
# https://www.codewars.com/kata/5b06c990908b7eea73000069/train/python

# 문제를 이해하기 어려웠다.
# 다른사람의 풀이
from math import log

def f(z, eps):
    if abs(z) >= 1.0: return -1
    return int(log(eps) / log(abs(z)))

def f1(z, eps):
    return max(-1, log(eps, abs(z)))


def dotest(z, eps, exp):
    print("z   = %.2f + %.2f * I" % (z.real, z.imag))
    print("eps = %.2e" % (eps))
    ans = f(z, eps)
    print("ACTUAL = %d" % (ans))
    print("EXPECT = %d" % (exp))
    e = abs(ans - exp) <= 1
    print(e, True)

dotest(complex(0.64, 0.75), 1e-12, 1953)
dotest(complex(30.0, 50.0), 1e-4, -1)
dotest(complex(0.3, 0.5), 1e-4, 17)
dotest(complex(0.13, 0.54), 1e-4, 15)