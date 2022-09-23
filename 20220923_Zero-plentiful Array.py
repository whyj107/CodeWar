# Zero-plentiful Array
# https://www.codewars.com/kata/59e270da7997cba3d3000041/train/python

# 나의 풀이
from itertools import groupby
def zero_plentiful(arr):
    result = [len(list(g)) > 3 for k, g in groupby(arr) if k == 0]
    return all(result) * len(result)

# 다른 사람의 풀이
import re
def zero_plentiful1(arr):
    s = ''.join(str(i) if i == 0 else '1' for i in arr)
    if sum(1 for i in re.findall(r'(?<!0)0{0,3}(?!0)', s) if i!=''):
        return 0
    return len(re.findall(r'0{4,}', s))

print(zero_plentiful([3]), 0)
print(zero_plentiful([0, 0, 0, 0, 0, 0]), 1)