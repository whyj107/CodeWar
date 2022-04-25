# Narcissistic Numbers
# https://www.codewars.com/kata/56b22765e1007b79f2000079/train/python

# 나의 풀이
def is_narcissistic(i):
    return sum([pow(int(j), len(str(i))) for j in str(i)]) == i

# 다른 사람의 풀이
def is_narcissistic1(n):
    num = str(n)
    length = len(num)
    return sum(int(a) ** length for a in num) == n

print(is_narcissistic(153), True)
print(is_narcissistic(201), False)
print(is_narcissistic(259), False)
print(is_narcissistic(371), True)
print(is_narcissistic(407), True)
print(is_narcissistic(595), False)
print(is_narcissistic(825), False)
print(is_narcissistic(1634), True)