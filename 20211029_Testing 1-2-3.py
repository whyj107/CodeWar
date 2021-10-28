# Testing 1-2-3
# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

# 나의 풀이
def number(lines):
    return [f'{index+1}: {i}' for index, i in enumerate(lines)]

# 다른 사람의 풀이
def number1(lines):
  return ['%d: %s' % v for v in enumerate(lines, 1)]

print(number([]), [])
print(number(["a", "b", "c"]), ["1: a", "2: b", "3: c"])