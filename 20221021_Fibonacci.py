# Fibonacci
# https://www.codewars.com/kata/57a1d5ef7cb1f3db590002af/train/python

# 나의 풀이
def fibonacci(n: int):
    fibo = [0] * (n+2)
    fibo[1] = 1
    for i in range(2, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
    return fibo[n]

# 다른 사람의 풀이
def fibonacci1(n: int) -> int:
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x

print(fibonacci(0), 0)
print(fibonacci(1), 1)
print(fibonacci(2), 1)
print(fibonacci(3), 2)
print(fibonacci(4), 3)
print(fibonacci(5), 5)
print(fibonacci(6), 8)
print(fibonacci(34), 5702887)
print(fibonacci(299), 137347080577163115432025771710279131845700275212767467264610201)

