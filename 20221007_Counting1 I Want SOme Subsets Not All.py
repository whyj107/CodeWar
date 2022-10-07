# Counting 1: I Want Some Subsets, Not All!
# https://www.codewars.com/kata/591392af88a4994caa0000e0/train/python

# 풀이
def f(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b + 1
    return a

print(f(5), 12)
print(f(3), 4)
print(f(2), 2)
print(f(20), 17710)