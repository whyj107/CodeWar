# BASIC: Making Six Toast.
# https://www.codewars.com/kata/5834fec22fb0ba7d080000e8/train/python

# 나의 풀이
def six_toast(num):
    return num-6 if num > 5 else 6-num%6

# 다른 사람의 풀이
def six_toast1(num):
    return abs(num-6)

print(six_toast(15), 9)
print(six_toast(6), 0)
print(six_toast(3), 3)
print(six_toast(5), 1)