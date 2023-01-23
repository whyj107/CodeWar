# Sum of Cubes
# https://www.codewars.com/kata/59a8570b570190d313000037/train/python

# 나의 풀이
def sum_cubes(n):
    return sum(i**3 for i in range(1, n+1))

# 다른 사람의 풀이
def sum_cubes1(n):
    return (n*(n+1)//2)**2

print(sum_cubes(1), 1)
print(sum_cubes(2), 9)
print(sum_cubes(3), 36)
print(sum_cubes(4), 100)
print(sum_cubes(10), 3025)
print(sum_cubes(123), 58155876)
