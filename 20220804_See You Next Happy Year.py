# See You Next Happy Year
# https://www.codewars.com/kata/5ae7e3f068e6445bc8000046/train/python

# 나의 풀이
def next_happy_year(year):
    year += 1
    while len(set(str(year))) != 4:
        year += 1
    return year

# 다른 사람의 풀이
from itertools import count
happy = lambda x: len(str(x)) == len(set(str(x)))
def next_happy_year1(year):
    return next(filter(happy, count(year+1)))

import re
def next_happy_year2(year):
    return year + 1 if re.match(r'(?:([0-9])(?!.*\1)){4}', str(year + 1)) else next_happy_year(year + 1)

print(next_happy_year(1001), 1023)
print(next_happy_year(1123), 1203)
print(next_happy_year(2001), 2013)
print(next_happy_year(2334), 2340)
print(next_happy_year(3331), 3401)
print(next_happy_year(1987), 2013)
print(next_happy_year(5555), 5601)
print(next_happy_year(7712), 7801)
print(next_happy_year(8088), 8091)
print(next_happy_year(8999), 9012)