# Reverse a number in any base
# https://www.codewars.com/kata/6469e4c905eaefffd44b6504/train/python

# 나의 풀이
def reverse_number(n, c):
    tmp = []
    if c == 1: return n
    while n >= c:
        n, b = divmod(n, c)
        tmp.append(b)
    tmp.append(n)

    result = 0
    for idx, _ in enumerate(tmp[::-1]):
        result += (_*pow(c, idx))
    return result

# 다른 사람의 풀이
def reverse_number2(n: int, b: int) -> int:
    if b == 1: return n
    res = 0
    while n > 0:
        res *= b
        res += n % b
        n //= b
    return res

testcases = [(12, 2, 3),
             (10, 5, 2),
             (45, 30, 451),
             (3, 4, 3),
             (5, 1, 5)]
for n, b, out in testcases:
    print(reverse_number(n, b), out)