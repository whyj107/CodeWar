# Eliminate the intruders! Bit manipulation
# https://www.codewars.com/kata/5a0d38c9697598b67a000041/train/python

# 나의 풀이
def eliminate_unset_bits(number):
    tmp = number.replace('0', '')
    return int(tmp, 2) if tmp else 0

# 나의 풀이
def eliminate_unset_bits1(string):
    return 2 ** (string.count('1')) - 1

def eliminate_unset_bits2(number):
    return int("0" + number.replace("0", ""), 2)

print(eliminate_unset_bits("11010101010101"), 255)
print(eliminate_unset_bits("111"), 7)
print(eliminate_unset_bits("1000000"), 1)
print(eliminate_unset_bits("000"), 0)