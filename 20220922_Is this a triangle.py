# Is this a tirangle?
# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

# 나의 풀이
# 삼각형 : 나머지 두 변의 길이의 합이 가장 긴 변의 길이보다 길다
def is_triangle(a, b, c):
    max_n = max(a, b, c)
    if a+b+c - max_n > max_n:
        return True
    return False

# 다른 사람의 풀이
def is_triangle1(a, b, c):
    return (a < b+c) and (b < a+c) and (c < a+b)

def is_triangle2(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

print(is_triangle(1, 2, 2), True)
print(is_triangle(7, 2, 2), False)
print(is_triangle(1, 2, 3), False)
print(is_triangle(1, 3, 2), False)
print(is_triangle(3, 1, 2), False)
print(is_triangle(5, 1, 2), False)
print(is_triangle(1, 2, 5), False)
print(is_triangle(2, 5, 1), False)
print(is_triangle(4, 2, 3), True)
print(is_triangle(5, 1, 5), True)
print(is_triangle(2, 2, 2), True)
print(is_triangle(-1, 2, 3), False)
print(is_triangle(1, -2, 3), False)
print(is_triangle(1, 2, -3), False)
print(is_triangle(0, 2, 3), False)