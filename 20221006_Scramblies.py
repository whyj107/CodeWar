# Scramblies
# https://www.codewars.com/kata/55c04b4cc56a697bb0000048/train/python

# 나의 풀이
from collections import Counter
def scramble(s1, s2):
    return len(Counter(s2) - Counter(s1)) == 0

# 다른 사람의 풀이
def scramble1(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))

for s1, s2, expected in [
    ('rkqodlw', 'world', True),
    ('cedewaraaossoqqyt', 'codewars', True),
    ('katas', 'steak', False),
    ('scriptjava', 'javascript', True),
    ('scriptingjava', 'javascript', True)
]:
    print(scramble(s1, s2), expected)

s1 = "abcdefghijklmnopqrstuvwxyz" * 10_000
s2 = "zyxcba" * 9_000
print(scramble(s1, s2), True)

print(scramble('sooo', 'oooos'), False)