# Simple remove duplicates
# https://www.codewars.com/kata/5ba38ba180824a86850000f7/train/python

# 나의 풀이
def solve(arr):
    result = []
    for a in arr[::-1]:
        if not a in result:
            result.append(a)
    return result[::-1]

# 다른 사람의 풀이
def solve1(arr):
    return list(dict.fromkeys(arr[::-1]))[::-1]

print(solve([3, 4, 4, 3, 6, 3]), [4, 6, 3])
print(solve([1, 2, 1, 2, 1, 2, 3]), [1, 2, 3])
print(solve([1, 2, 3, 4]), [1, 2, 3, 4])
print(solve([1, 1, 4, 5, 1, 2, 1]), [4, 5, 2, 1])