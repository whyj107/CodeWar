# Sum The Strings
# https://www.codewars.com/kata/5966e33c4e686b508700002d/train/python

# 나의 풀이
def sum_str(a, b):
    if not a.isnumeric(): a = "0"
    if not b.isnumeric(): b = "0"
    return str(int(a) + int(b))

# 다른 사람의 풀이
def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))

print(sum_str("4", "5"), "9")
print(sum_str("34", "5"), "39")
print(sum_str("9", ""), "9")
print(sum_str("", "9"), "9")
print(sum_str("", ""), "0")