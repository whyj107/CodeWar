# Hands Up
# https://www.codewars.com/kata/56d8f14cba01a83cdb0002a2/train/python

# 풀이
def get_positions(n):
    return n % 3, n // 3 % 3, n // 9 % 3

def get_positions1(n):
    return tuple(n // d % 3 for d in (1, 3, 9))

print(get_positions(54), (0, 0, 0))
print(get_positions(98), (2, 2, 1))
print(get_positions(3), (0, 1, 0))