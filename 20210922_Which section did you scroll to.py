# Whick section did you scroll to?
# https://www.codewars.com/kata/5cb05eee03c3ff002153d4ef/train/python

# 나의 풀이
def get_section_id(scroll, sizes):
    pre = 0
    for idx, s in enumerate(sizes):
        if pre <= scroll < pre+s:
            return idx
        pre += s
    return -1

# 다른 사람의 풀이
from itertools import accumulate
def get_section_id1(scroll, sizes):
    return next((i for i,x in enumerate(accumulate(sizes)) if x > scroll), -1)

print(get_section_id(299, [300, 200, 400, 600, 100]), 0)
print(get_section_id(300, [300, 200, 400, 600, 100]), 1)
print(get_section_id(1600, [300, 200, 400, 600, 100]), -1)