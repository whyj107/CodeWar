# Grains
# https://www.codewars.com/kata/55f7eb009e6614447b000099/train/python

# 나의 풀이
def square(number):
    return 2**(number-1)

# 다른 사람의 풀이
def square1(n):
    return 1 << n-1

print(square(1), 1)
print(square(3), 4)
print(square(4), 8)
print(square(16), 32768)
print(square(32), 2147483648)
