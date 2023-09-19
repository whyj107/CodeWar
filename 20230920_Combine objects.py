# Combine objects
# https://www.codewars.com/kata/56bd9e4b0d0b64eaf5000819/train/python

# 나의 풀이
def combine(*args):
    r = {}
    for i in args:
        for k, v in i.items():
            r.setdefault(k, 0)
            r[k] += v
    return r

# 다른 사람의 풀이
def combine1(*bs):
    c = {}
    for b in bs:
        for k, v in b.items():
            c[k] = v + c.get(k, 0)
    return c