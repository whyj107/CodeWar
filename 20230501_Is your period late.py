# Is your period late?
# https://www.codewars.com/kata/578a8a01e9fd1549e50001f1/train/python

# 나의 풀이
from datetime import date
def period_is_late(last,today,cycle_length):
    return (today - last).days > cycle_length

print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28), True)
print(period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35), False)
print(period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28), False)
print(period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28), False)
print(period_is_late(date(2016, 7, 12), date(2016, 8, 10), 28), True)
print(period_is_late(date(2016, 7, 1), date(2016, 8, 1), 30), True)
print(period_is_late(date(2016, 6, 1), date(2016, 6, 30), 30), False)
print(period_is_late(date(2016, 1, 1), date(2016, 1, 31), 30), False)
print(period_is_late(date(2016, 1, 1), date(2016, 2, 1), 30), True)
