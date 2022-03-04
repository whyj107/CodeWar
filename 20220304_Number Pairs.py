# Number Pairs
# 7kyu
# https://www.codewars.com/kata/563b1f55a5f2079dc100008a/train/python

# 나의 풀이
def get_larger_numbers(a, b):
    return [max(i, j) for i, j in zip(a, b)]

# 다른 사람의 풀이
def get_larger_numbers1(a, b):
    return map(max, a, b)

a = [13, 64, 15, 17, 88]
b = [23, 14, 53, 17, 80]
print(get_larger_numbers(a, b), [23, 64, 53, 17, 88])

a = [34, -64, 15, 17, 88]
b = [23, 14, 53, 17, 80]
print(get_larger_numbers(a, b), [34, 14, 53, 17, 88])
