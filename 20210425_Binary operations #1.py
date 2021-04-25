# Binary operations #1
# https://www.codewars.com/kata/560e80734267381a270000a2/train/python

# 다른 사람의 풀이
def flip_bit(value, bit_index):
    return value ^ (1 << (bit_index-1))

def flip_bit1(v, b):
    return 1<<b-1 ^ v

print(flip_bit(0, 16), 1 << 15)
print(flip_bit((1<<31)-1, 31), (1 << 30)-1)
print(flip_bit(127, 8), 0xFF)
