# Century From Year
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/python

# 나의 풀이
def century(year):
    return (year + 99) // 100

# 다른 사람의 풀이
def century1(year):
    return (year - 1) // 100 + 1

from math import ceil

def century2(year):
    return ceil(year / 100)

print(century(1705), 18)
print(century(1900), 19)
print(century(1601), 17)
print(century(2000), 20)
print(century(356), 4)
print(century(89), 1)
