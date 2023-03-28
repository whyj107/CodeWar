# Sums of consecutive integers
# https://www.codewars.com/kata/55b54be931e9ce28bc0000d6/train/python

# 나의 풀이
def position(x, y, n):
    return n - (x//2-(1 if not x%2 else 0)) + y//x

# 다른 사람의 풀이
def position1(x,y,n):
    return (y - sum(range(x)))//x + n

print(position(4, 14, 3), 5)
print(position(2, 25, 0), 12)
print(position(7, 749, 5), 109)
print(position(3, -9, 1), -3)
print(position(5, 0, 0), -2)