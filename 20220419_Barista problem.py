# Barista problem
# https://www.codewars.com/kata/6167e70fc9bd9b00565ffa4e/train/python

# 나의 풀이
def barista(coffees):
    coffees = sorted(coffees)
    return sum(sum(coffees[:i+1]) + i*2 for i in range(len(coffees)))

# 다른 사람의 풀이
from itertools import accumulate
def barista1(coffees):
    return sum(accumulate(sorted(coffees), lambda a,c:a+2+c ))

print(barista([]), 0)
print(barista([2, 10, 5, 3, 9]), 85)
print(barista([4, 3, 2]), 22)
print(barista([20, 5]), 32)
print(barista([20, 5, 4, 3, 1, 5, 7, 8]), 211)
print(barista([5, 4, 3, 2, 1]), 55)