# Walking in the hallway
# https://www.codewars.com/kata/6368426ec94f16a1e7e137fc/train/python

# 나의 풀이
from math import ceil
def contact(hallway):
    left = False
    space = 0
    result = []
    for h in hallway:
        if h == '>':
            left = True
        if left:
            space += 1
            if h == '<':
                result.append(ceil(space/2))
                space = 0
                left = False
            elif h == '>':
                space = 0
    return min(result) if not result == [] else -1

# 다른 사람의 풀이
import re
def contact1(hallway):
    gaps = re.findall(r'>-*<', hallway)
    return min(map(len, gaps), default=-2) >> 1

sample_tests = [
    ('---><---', 1),
    ('--->-<------->----<-', 1),
    ('----<----->----', -1),
    ('>-----<-->--<-----', 2),
    ('>>-----<<', 3),
    ('---><---', 1),
    (
    '>---------------<--------------------------<-------->---------<------->----------<----<---->>----------<------->>>---------------<<------>',
    5)
]

for hallway, expected in sample_tests:
    print(contact(hallway), expected)