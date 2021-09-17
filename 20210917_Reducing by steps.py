# Reducing by steps
# https://www.codewars.com/kata/56efab15740d301ab40002ee/train/python

# 나의 풀이
from math import gcd
from functools import reduce
def gcdi(x, y):
    return gcd(abs(x), abs(y))
def lcmu(a, b):
    return abs(a)*abs(b)//gcdi(a, b)
def som(a, b):
    return a+b
def maxi(a, b):
    return max(a, b)
def mini(a, b):
    return min(a, b)
def oper_array0(fct, arr, init):
    print()
    result = []
    for a in arr:
        init = fct(a, init)
        result.append(init)
    return result
def oper_array(fct, arr, init):
    return [reduce(fct, [init, *arr[:i+1]]) for i in range(len(arr))]

def testing(actual, expected):
    print(actual, expected)

a = [18, 69, -90, -78, 65, 40]
r = [18, 3, 3, 3, 1, 1]
op = oper_array(gcdi, a, a[0])
testing(op, r)
r = [18, 414, 2070, 26910, 26910, 107640]
op = oper_array(lcmu, a, a[0])
testing(op, r)
r = [18, 87, -3, -81, -16, 24]
op = oper_array(som, a, 0)
testing(op, r)
r = [18, 18, -90, -90, -90, -90]
op = oper_array(mini, a, a[0])
testing(op, r)
r = [18, 69, 69, 69, 69, 69]
op = oper_array(maxi, a, a[0])
testing(op, r)
