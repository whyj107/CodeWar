# Simple Fun #302: Find The Max Sum
# https://www.codewars.com/kata/59252121fb1f93fc8200013a/train/python

# 나의 풀이
# (a1 + a2) % 2 == 0
# (a2 + a3) % 3 == 0
# (a1 + a2 + a3) % 5 == 0

def find_max_sum(n):
    if n%2==0 and n%3==0 and n%5==0: return n*3
    a1, a2, a3 = n, n, n
    while (a1+a2)%2!=0 or (a2+a3)%3!=0 or (a1+a2+a3)%5!=0:
        if (a1+a2)%2!=0:
            a1 -= 1
        while (a2+a3)%3!=0:
            a3 -= 1

        if (a1+a2+a3)%5 == 2:
            a1 -= 2

        if (a1+a2+a3)%5!=0:
            a2 -= 1
            a1, a3 = n, n
    return a1+a2+a3

# 다른 사람의 풀이
from collections import deque
def find_max_sum2(n):
    q = deque([(n,n,n)])
    while q:
        a,b,c = q.popleft()
        if (a+b)%2 == 0 and (b+c)%3 == 0 and (a+b+c)%5 == 0:
            return a+b+c
        q.append((a-1,b,c))
        q.append((a,b-1,c))
        q.append((a,b,c-1))

test_cases = [
    (0, 0), (3, 5), (4, 10), (5, 10),
    (6, 15), (7, 15), (8, 20), (9, 25),
    (30, 90), (29, 85), (28, 80), (10000, 29995),
]

for n, expected in test_cases:
    print(find_max_sum(n), expected, f'{n=}')