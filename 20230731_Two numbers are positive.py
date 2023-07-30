# Two numbers are positive
# https://www.codewars.com/kata/602db3215c22df000e8544f0/train/python

def two_are_positive(a, b, c):
    return sum([a>0, b>0, c>0]) == 2

# 다른 사람의 풀이
def two_are_positive1(*args):
    return sum(x > 0 for x in args) == 2

print(two_are_positive(2, 4, -3), True, "(2, 4, -3)")
print(two_are_positive(-4, 6, 8), True, "(-4, 6, 8)")
print(two_are_positive(4, -6, 9), True, "(4, -6, 9)")
print(two_are_positive(4, 6, 0), True, "(4, 6, 0)")
print(two_are_positive(-4, 6, 0), False, "(-4, 6, 0)")
print(two_are_positive(4, 6, 10), False, "(4, 6, 10)")
print(two_are_positive(-14, -3, -4), False, "(-14, -3, -4)")



