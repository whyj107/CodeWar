# Where's my Elements at?
# https://www.codewars.com/kata/5a0ec343c374cb6da0000006/train/python

# 나의 풀이
def element_location(begin: int, end: int, index: int, size: int) -> int:
    r = begin + index*size
    if begin == r: return begin
    if r >= end or r <= begin or index < 0:
        raise IndexError()
    else:
        return r

# 다른 사람의 풀이
def element_location1(begin: int, end: int, index: int, size: int) -> int:
    out = begin + index * size
    if out < begin or out >= end:
        raise IndexError
    return out

print(element_location(0x1000, 0x1040, 0x3, 0x8), 0x1018)
print(element_location(0x2000, 0x2100, 0x3, 0x4), 0x200C)
print(element_location(0x2000, 0x2100, 0x0, 0x4), 0x2000)
