# Simple Fun #141: Hamming Distance
# https://www.codewars.com/kata/58a6af7e8c08b1e9c40001c1/train/python

# 나의 풀이
def hamming_distance(a, b):
    a = bin(a).lstrip('0b')
    b = bin(b).lstrip('0b')
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))
    return sum(i!=j for i, j in zip(a, b))

# 다른 사람의 풀이
def hamming_distance(a, b):
    return bin(a ^ b).count('1')

print(hamming_distance(25, 87), 4)
print(hamming_distance(256, 302), 4)
print(hamming_distance(543, 634), 4)
print(hamming_distance(34013, 702), 7)