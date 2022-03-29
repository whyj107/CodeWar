# Alphabetical Grid
# https://www.codewars.com/kata/60a94f1443f8730025d1744b/train/python

# 나의 풀이
from string import ascii_lowercase
from collections import deque
def grid(N):
    alpha = deque(ascii_lowercase)
    result = []
    for _ in range(N):
        tmp = [alpha[j % 26] for j in range(N)]
        result.append(' '.join(tmp))
        alpha.append(alpha.popleft())
    return None if N < 0 else '\n'.join(result)

# 다른 사람의 풀이
def grid1(n):
    if n >= 0:
        return '\n'.join( ' '.join( chr(97+(i+j)%26)
                                   for i in range(n) )
                         for j in range(n) )

print(grid(0), '')
print(grid(1), 'a')
print(grid(2), 'a b\nb c')
print(grid(4), 'a b c d\nb c d e\nc d e f\nd e f g')
print(grid(6), 'a b c d e f\nb c d e f g\nc d e f g h\nd e f g h i\ne f g h i j\nf g h i j k')
print(grid(-1), None)
print(grid(-5), None)