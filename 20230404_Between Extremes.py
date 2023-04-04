# Between Extremes
# https://www.codewars.com/kata/56d19b2ac05aed1a20000430/train/python

# 나의 풀이
def between_extremes(numbers):
    return max(numbers) - min(numbers)


print(between_extremes([1, 1]), 0)
print(between_extremes([-1, -1]), 0)
print(between_extremes([1, -1]), 2)
print(between_extremes([21, 34, 54, 43, 26, 12]), 42)
print(between_extremes([-1, -41, -77, -100]), 99)