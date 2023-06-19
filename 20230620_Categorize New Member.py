# Categorize New Member
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

# 나의 풀이
def open_or_senior(data):
    return ["Senior" if d[0] >= 55 and d[1] > 7 else "Open" for d in data ]

print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]), ['Open', 'Senior', 'Open', 'Senior'])
print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]), ['Open', 'Open', 'Senior', 'Open'])