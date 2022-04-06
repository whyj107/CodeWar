# Binary Representation of an Integer
# https://www.codewars.com/kata/5a5f3034cadebf76db000023/train/python

# 나의 풀이
def show_bits(n):
    return [(n>>i)&1 for i in range(31, -1, -1)]

# 다른 사람의 풀이
def showBits1(n):
    return list(map(int, '{:032b}'.format(n if n >= 0 else 2**32 + n)))

def showBits2(n):
    return [int((1 << i) & n > 0) for i in range(32)][::-1]

_ar_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1]
print(show_bits(701) == _ar_)

_ar_ = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1]
print(show_bits(-245) == _ar_)

_ar_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
print(show_bits(12336) == _ar_)