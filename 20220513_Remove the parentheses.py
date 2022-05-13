# Remove the parentheses
# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/train/python

# 나의 풀이
from collections import deque

def remove_parentheses(s):
    d = deque()
    result = ''
    for i in s:
        if i == '(':
            d.append('(')
        elif i == ')':
            d.pop()
        else:
            if len(d) == 0:
                result += i
    return result

# 다른 사람의 풀이
def remove_parentheses1(s):
    lvl,out = 0,[]
    for c in s:
        lvl += c=='('
        if not lvl: out.append(c)
        lvl -= c==')'
    return ''.join(out)

import re
def remove_parentheses2(s):
    while (t := re.sub(r'\([^()]*\)', '', s)) != s:
        s = t
    return s

print(remove_parentheses("example(unwanted thing)example"), "exampleexample")
print(remove_parentheses("example (unwanted thing) example"), "example  example")
print(remove_parentheses("a (bc d)e"), "a e")
print(remove_parentheses("a(b(c))"), "a")
print(remove_parentheses("hello example (words(more words) here) something"), "hello example  something")
print(remove_parentheses("(first group) (second group) (third group)"), "  ")