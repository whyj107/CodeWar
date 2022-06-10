# Chain me
# https://www.codewars.com/kata/54fb853b2c8785dd5e000957/train/python

# 나의 풀이
def chain(init_val, functions):
    result = init_val
    for f in functions:
        result = f(result)
    return result

# 다른 사람의 풀이
from functools import reduce
def chain1(init_val, functions):
    return reduce(lambda x, f: f(x), functions, init_val)

def add10(x): return x + 10
def mul30(x): return x * 30


print(chain(42, []), 42)
print(chain(50, [mul30]), 1500)
print(chain(50, [mul30, add10]), 1510)
print(chain(50, [add10, mul30]), 1800)
