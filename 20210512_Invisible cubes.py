# Invisible cubes
# https://www.codewars.com/kata/560d6ebe7a8c737c52000084/train/python

# 문제가 이해되지 않는다....
# 풀이
def not_visible_cubes(n):
    return max(n-2, 0)**3

print(not_visible_cubes(0), 0)
print(not_visible_cubes(1), 0)
print(not_visible_cubes(2), 0)
print(not_visible_cubes(3), 1)
print(not_visible_cubes(4), 8)