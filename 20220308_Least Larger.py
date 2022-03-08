# Least Larger
# https://www.codewars.com/kata/5f8341f6d030dc002a69d7e4/train/python

# 나의 풀이
def least_larger(a, i):
    result = [(idx, j) for idx, j in enumerate(a) if j > a[i]]
    return min(result, key=lambda x: x[1])[0] if result != [] else -1

# 다른 사람의 풀이
def least_larger1(a, i):
    b = [x for x in a if x>a[i]]
    return a.index(min(b)) if b else -1

print(least_larger([4, 1, 3, 5, 6], 0), 3)
print(least_larger([4, 1, 3, 5, 6], 4), -1)
print(least_larger([1, 3, 5, 2, 4], 0), 3)
