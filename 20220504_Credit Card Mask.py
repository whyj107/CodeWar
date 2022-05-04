# Credit Card Mask
# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

# 나의 풀이
def maskify(cc):
    return ('' if len(cc) < 5 else '#'*(len(cc)-4)) + cc[-4:]

# 다른 사람의 풀이
def maskify1(cc):
    return "#"*(len(cc)-4) + cc[-4:]

print(maskify(''), '')
print(maskify('123'), '123')
print(maskify('SF$SDfgsd2eA'), '########d2eA')