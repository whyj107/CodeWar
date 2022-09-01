# Exes and Ohs
# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

# 나의 풀이
def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

print(xo('xo'), 'True expected')
print(xo('xo0'), 'True expected')
print(xo('xxxoo'), 'False expected')
