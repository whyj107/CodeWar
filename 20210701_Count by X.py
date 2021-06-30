# Count by X
# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

# 나의 풀이
def count_by(x, n):
    return list(range(x, x*n+1, x))

# 다른 사람의 풀이
def count_by1(x, n):
    return range(x, x*n+1, x)

print(count_by(1, 5), [1, 2, 3, 4, 5])
print(count_by(2, 5), [2, 4, 6, 8, 10])
print(count_by(3, 5), [3, 6, 9, 12, 15])
print(count_by(50, 5), [50, 100, 150, 200, 250])
print(count_by(100, 5), [100, 200, 300, 400, 500])