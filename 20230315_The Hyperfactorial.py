# The Hyperfactorial
# https://www.codewars.com/kata/6324786fcc1a9700260a2147/train/python

# 나의 풀이
def hyperfact(n):
    return n<1 or ((n**n)*hyperfact(n-1))%1000000007

# 다른 사람의 풀이
# prod는 객체의 행이나 열의 곱을 구하는 메서드입니다.
from math import prod
def hyperfact1(n, m=1_000_000_007):
    return prod(pow(i, i) for i in range(1, n+1)) % m

print(hyperfact(1), 1)
print(hyperfact(2), 4)
print(hyperfact(3), 108)
print(hyperfact(4), 27648)
print(hyperfact(5), 86400000)
print(hyperfact(6), 78371783)
print(hyperfact(7), 532835375)
print(hyperfact(8), 116239542)
print(hyperfact(9), 887540985)
print(hyperfact(10), 872131491)
print(hyperfact(300), 19936859)