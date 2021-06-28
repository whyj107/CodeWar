# Compare within margin
# https://www.codewars.com/kata/56453a12fcee9a6c4700009c/train/python

# 나의 풀이
def close_compare(a, b, margin=0):
    return 0 if abs(a-b) <= margin and margin!=0 else (-1 if a < b else(1 if a > b else 0))

# 다른 사람의 풀이
def close_compare(a, b, margin = 0):
    return 0 if abs(a - b) <= margin else -1 if b > a else 1

print(close_compare(4, 5), -1)
print(close_compare(5, 5), 0)
print(close_compare(6, 5), 1)

print(close_compare(2, 5, 3), 0)
print(close_compare(5, 5, 3), 0)
print(close_compare(8, 5, 3), 0)
print(close_compare(8.1, 5, 3), 1)
print(close_compare(1.99, 5, 3), -1)