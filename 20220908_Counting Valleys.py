# Counting Valleys
# https://www.codewars.com/kata/5da9973d06119a000e604cb6/train/python

# 나의 풀이
def counting_valleys(s):
    valley, level = 0, 0
    for i in s:
        if i == 'D':
            level -= 1
        elif i == 'U':
            level += 1
            if level == 0:
                valley += 1
    return valley

# 다른 사람의 풀이
def counting_valleys1(s):
    level, valleys = 0, 0
    for step in s:
        if step == 'U' and level == -1:
            valleys += 1
        level += {'U': 1, 'F': 0, 'D': -1}[step]
    return valleys

print(counting_valleys('UFFFD'), 0)
print(counting_valleys('DFFFD'), 0)
print(counting_valleys('UFFFU'), 0)
print(counting_valleys('DFFFU'), 1)
print(counting_valleys('UFFDDFDUDFUFU'), 1)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'), 2)
print(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'), 3)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 4)
print(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 6)