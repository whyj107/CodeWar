# SumFibs
# https://www.codewars.com/kata/56662e268c0797cece0000bb/train/python

# 나의 풀이
def sum_fibs(n):
    result = 0
    a, b = 0, 1
    for i in range(n-1):
        c = a+b
        a = b
        b = c
        if c % 2 == 0:
            result += c
    return result

# 다른 사람의 풀이
def sum_fibs1(n):
    res, x, y = 0, 2, 0
    for _ in range(n//3):
        res, x, y = res+x, 4*x+y, x
    return res

print(sum_fibs(5), 2)
print(sum_fibs(9), 44)
print(sum_fibs(10), 44)
print(sum_fibs(11), 44)
