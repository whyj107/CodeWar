# Number of Decimal Digits
# https://www.codewars.com/kata/58fa273ca6d84c158e000052/train/python

# 나의 풀이
def digits(n):
    return len(str(n))

# 다른 사람의 풀이
def digits1(n):
    digits = 1
    while n // 10 > 0:
        n //= 10
        digits += 1

    return digits

print(digits(5), 1)
print(digits(12345), 5)
print(digits(9876543210), 10)