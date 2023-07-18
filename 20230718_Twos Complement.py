# Two's Complement
# https://www.codewars.com/kata/58d4785a2285e7795c00013b/train/python

# 나의 풀이
def to_twos_complement(binary, bits):
    binary = binary.replace(' ', '')
    if binary[0] == '1':
        return (-1)*(2**bits + 1 - int(binary, 2)) + 1
    return int(binary, 2)

def from_twos_complement(n, bits):
    return bin(n & (2**bits-1))[2:].zfill(bits)


# 다른 사람의 풀이
def to_twos_complement1(binary, bits):
    return int(binary.replace(' ', ''), 2) - 2 ** bits * int(binary[0])

def from_twos_complement1(n, bits):
    return '{:0{}b}'.format(n & 2 ** bits - 1, bits)