# Yahtzee upper section scoring
# https://www.codewars.com/kata/63b4758f27f8e5000fc1e427/train/python

# 나의 풀이
from collections import Counter
def yahtzee_upper(dice):
    return max(k*v for k, v in Counter(dice).items())

# 다른 사람의 풀이
def yahtzee_upper1(dice:list)->int:
    return max([dice.count(x)*x for x in set(dice)])

from itertools import starmap
from operator import mul
def yahtzee_upper2(dice):
    return max(starmap(mul, Counter(dice).items()))

from math import prod
def yahtzee_upper3(dice):
    return max(map(prod, Counter(dice).items()))

print(yahtzee_upper([2, 3, 5, 5, 6]), 10)
print(yahtzee_upper([1, 1, 1, 1, 3]), 4)
print(yahtzee_upper([1, 1, 1, 3, 3]), 6)
print(yahtzee_upper([1, 2, 3, 4, 5]), 5)
print(yahtzee_upper([6, 6, 6, 6, 6]), 30)
print(yahtzee_upper([15, 9, 9, 8, 9]), 27)
print(yahtzee_upper([1654, 1654, 50995, 30864, 1654, 50995, 22747,
                  1654, 1654, 1654, 1654, 1654, 30864, 4868, 1654, 4868, 1654,
                  30864, 4868, 30864]), 123456)