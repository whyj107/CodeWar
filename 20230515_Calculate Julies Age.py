# Calculate Julie's Age
# https://www.codewars.com/kata/558445a88826e1376b000011/train/python

# 나의 풀이
# 동생 + x = 줄리
# 동생 * y = 줄리
def age(x, y):
    return x*y/(y-1)

# 다른 사람의 풀이
def age1(x, y):
    return x / (y - 1) + x

print(round(age(-15, 0.25)), 5)
print(round(age(6, 3)), 9)