# What is between?
# https://www.codewars.com/kata/55ecd718f46fba02e5000029/train/python

# 나의 풀이
def between(a, b):
    return list(range(a, b+1))

print(between(1, 4), [1, 2, 3, 4])
print(between(-2, 2), [-2, -1, 0, 1, 2])
