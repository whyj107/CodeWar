# Digital cypher
# https://www.codewars.com/kata/592e830e043b99888600002d/train/python

# 나의 풀이
def encode(message, key):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    keys = list(map(int, str(key)))
    return [alpha.index(m)+1 + keys[idx % len(str(key))] for idx, m in enumerate(message)]

# 다른 사람의 풀이
from itertools import cycle
def encode1(message, key):
    return [ord(a) - 96 + int(b) for a,b in zip(message,cycle(str(key)))]

print(encode("scout", 1939),
      [20, 12, 18, 30, 21])
print(encode("masterpiece", 1939),
      [14, 10, 22, 29, 6, 27, 19, 18, 6, 12, 8])