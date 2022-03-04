# Is the date today
# 8 kyu
# https://www.codewars.com/kata/563c13853b07a8f17c000022/train/python

# 나의 풀이
from datetime import datetime
def is_today(date):
    return datetime.today().date() == date.date()

# 다른 사람의 풀이
def is_today1(date):
    return datetime.today().strftime('%Y%m%d') == date.strftime('%Y%m%d')

print(is_today(datetime(2020, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime(2080, 10, 1, 1, 1, 1, 1)), False)
print(is_today(datetime.today()), True)