# The alphabet product
# https://www.codewars.com/kata/63b06ea0c9e1ce000f1e2407/train/python

# 나의 풀이
# a, b, c, d, ab, bc, cd, da
# 여기서 d가 무엇일까요
def alphabet(ns):
    ns = sorted(ns)
    a = ns.pop(0)
    b = ns.pop(0)
    ns.remove(a*b)
    c = ns.pop(0)
    ns.remove(b*c)
    return ns[-1]//c

# 다른 사람의 풀이
def alphabet1(ns):
    ns.sort()
    a = ns.pop(0)
    b = ns.pop(0)
    ns.remove(a * b)
    c = ns.pop(0)
    cd = ns.pop()
    return cd // c

print(alphabet([2, 3, 4, 1, 12, 6, 2, 4]), 4)
print(alphabet([2, 6, 7, 3, 14, 35, 15, 5]), 7)
print(alphabet([20, 10, 6, 5, 4, 3, 2, 12]), 5)
print(alphabet([2, 6, 18, 3, 6, 7, 42, 14]), 7)
print(alphabet([7, 96, 8, 240, 12, 140, 20, 56]), 20)
print(alphabet([20, 30, 6, 7, 4, 42, 28, 5]), 7)
print(alphabet([11340, 99, 3872, 44, 66528, 88, 15, 660]), 756)