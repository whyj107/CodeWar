# Fibonacci Rabbits
# https://www.codewars.com/kata/5559e4e4bbb3925164000125/train/python

# 나의 풀이
def fib_rabbits(n, b):
    imm_p = 1
    mat_p = 0
    for i in range(n):
        tmp_i = mat_p*b
        mat_p += imm_p
        imm_p = tmp_i
    return mat_p

# 다른 사람의 풀이
def fib_rabbits1(n, b):
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + b * x
    return x



print(fib_rabbits(5, 3), 19)
print(fib_rabbits(0, 4), 0)
print(fib_rabbits(1, 4), 1)
print(fib_rabbits(4, 0), 1)
print(fib_rabbits(6, 3), 40)
print(fib_rabbits(8, 12), 8425)
print(fib_rabbits(7, 4), 181)