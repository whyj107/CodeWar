# Hello World - WIthout Strings
# https://www.codewars.com/kata/584c7b1e2cb5e1a727000047/train/python

# 나의 풀이
def hello_world():
    tmp = [72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]
    return str().join([chr(t) for t in tmp])

print(hello_world(), 'Hello, World!')