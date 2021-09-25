# Adding remainders to a list
# https://www.codewars.com/kata/5acc3634c6fde760ec0001f7/train/python

# 나의 풀이
def solve(nums, div):
    return [n+(n % div) for n in nums]

print(solve([2, 7, 5, 9, 100, 34, 32, 0], 3), [4, 8, 7, 9, 101, 35, 34, 0])
print(solve([1000, 999, 998, 997], 5), [1000, 1003, 1001, 999])
print(solve([], 2), [])