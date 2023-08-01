# Replace every nth
# https://www.codewars.com/kata/57fcaed83206fb15fd00027a/train/python

# 나의 풀이
def replace_nth(text, n, old_value, new_value):
    r = ''
    idx = 0
    for t in text:
        if t == old_value:
            idx += 1
            if idx == n:
                r += new_value
                idx = 0
            else:
                r += t
        else:
            r += t
    return r

# 다른 사람의 풀이
def replace_nth1(text, n, old, new):
    count = 0
    res = ""
    for c in text:
        if c==old:
            count+=1
            if count ==n:
                res+=new
                count=0
                continue
        res+=c
    return res