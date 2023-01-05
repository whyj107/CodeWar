# MinMinMax
# https://www.codewars.com/kata/58d3487a643a3f6aa20000ff/train/python

# 나의 풀이
def min_min_max(arr):
    min_n = min(arr)
    max_n = max(arr)
    n = min_n + 1
    while n in arr:
        n += 1
    return [min_n, n, max_n]

# 다른 사람의 풀이
def minMinMax1(arr):
    s, mi, ma = set(arr), min(arr), max(arr)
    return [mi, next(x for x in range(mi+1, ma) if x not in s), ma]

print(min_min_max([-1, 4, 5, -23, 24]), [-23, -22, 24])
print(min_min_max([1, 3, -3, -2, 8, -1]), [-3, 0, 8])
print(min_min_max([2, -4, 8, -5, 9, 7]), [-5, -3, 9])
