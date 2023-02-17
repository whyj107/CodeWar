# Integer depth
# https://www.codewars.com/kata/59b401e24f98a813f9000026/train/python

# 나의 풀이
def compute_depth(n):
    result = set()
    i = 0
    while len(result) != 10:
        i += 1
        result = result | set(map(int, str(i*n)))
    return i

# 다른 사람의 풀이
def compute_depth1(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i

print(compute_depth(1), 10)
print(compute_depth(42), 9)
