# Handshake problem
# https://www.codewars.com/kata/5574835e3e404a0bed00001b/train/python

# 나의 풀이
# n(n-1)/2 = handshakes
from math import ceil, sqrt
def get_participants(handshakes):
    return ceil((1+sqrt(1+8*handshakes))/2) if handshakes != 0 else 0

print(get_participants(0), 0)
print(get_participants(1), 2)
print(get_participants(3), 3)
print(get_participants(6), 4)
print(get_participants(7), 5)
print(get_participants(8), 5)
print(get_participants(9), 5)
print(get_participants(10), 5)