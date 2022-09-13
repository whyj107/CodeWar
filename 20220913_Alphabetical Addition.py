# Alphabetical Addition
# https://www.codewars.com/kata/5d50e3914861a500121e1958/train/python

# 나의 풀이
def add_letters(*letters):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    result = len(alpha)-1
    for letter in letters:
        result += (alpha.index(letter)+1)
    return alpha[result%len(alpha)]

# 다른 사람의 풀이
def add_letters1(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)

from string import ascii_lowercase
def add_letters2(*letters):
  return ascii_lowercase[sum(ascii_lowercase.index(c) + 1 for c in letters) % 26 - 1]

tests = [
    (['a', 'b', 'c'], 'f'),
    (['z'], 'z'),
    (['a', 'b'], 'c'),
    (['c'], 'c'),
    (['z', 'a'], 'a'),
    (['y', 'c', 'b'], 'd'),
    ([], 'z')
]
for i, o in tests:
    str = ', '.join(['"' + s + '"' for s in i])
    print(add_letters(*i), o)