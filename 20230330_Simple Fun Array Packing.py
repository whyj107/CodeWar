# Simple Fun #9: Array Packing
# https://www.codewars.com/kata/588453ea56daa4af920000ca/train/python

# 나의 풀이
def array_packing(arr):
    return int(''.join(bin(a)[2:].zfill(8) for a in arr[::-1]),2)

# 다른 사람의 풀이
def array_packing1(arr):
    return int.from_bytes(arr, 'little')

def array_packing2(arr):
    return int(''.join('{:08b}'.format(n) for n in reversed(arr)), 2)

print(array_packing([24, 85, 0]), 21784)
print(array_packing([23, 45, 39]), 2567447)
print(array_packing([1, 1]), 257)
print(array_packing([0]), 0)
print(array_packing([255, 255, 255, 255]), 4294967295)