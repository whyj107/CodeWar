# String incrementer
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

# 나의 풀이
def increment_string(strng):
    n, r = '', ''
    for s in strng[::-1]:
        if s.isdecimal():
            n += s
        else:
            r = strng[:-len(n)]
            break
    if not n == '':
        p = 1
        tmp = ''
        for i in n:
            if int(i)+p > 9:
                tmp += '0'
                p = 1
            else:
                tmp += str(int(i)+p)
                p = 0
        if p: tmp += '1'
        return f'{r}{tmp[::-1]}'
    else:
        return f'{strng}1'

# 다른 사람의 풀이
def increment_string1(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))

import re
def increment_string2(strng):
    m = re.match('^(.*?)(\d+)$', strng)
    name, num = (m.group(1), m.group(2)) if m else (strng, '0')
    return '{0}{1:0{2}}'.format(name, int(num)+1, len(num))

print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")
print(increment_string("foobar00"), "foobar01")
print(increment_string("foobar99"), "foobar100")
print(increment_string("foobar099"), "foobar100")
print(increment_string("fo99obar99"), "fo99obar100")
print(increment_string(""), "1")