# Converting 12-hour time to 24-hour time
# https://www.codewars.com/kata/59b0a6da44a4b7080300008a/train/python

# 나의 풀이
def to24hourtime(hour, minute, period):
    hour -= 12 if hour == 12 else 0
    hour += 12 if period == 'pm' else 0
    return f'{hour:02}{minute:02}'

# 다른 사람의 풀이
def solve(h, m, p):
    return '%02d%02d' % (h % 12 + 12 * (p == 'pm'), m)

print(to24hourtime(1, 0, 'am'), '0100')
print(to24hourtime(1, 0, 'pm'), '1300')
print(to24hourtime(12, 0, 'am'), '0000')
print(to24hourtime(12, 0, 'pm'), '1200')
print(to24hourtime(6, 30, 'am'), '0630')
print(to24hourtime(9, 45, 'pm'), '2145')
