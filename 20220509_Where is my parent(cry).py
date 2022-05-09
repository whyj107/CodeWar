# Where is my parent!?(cry)
# https://www.codewars.com/kata/58539230879867a8cd00011c/train/python

# 나의 풀이
def find_children(dancing_brigade):
    result = sorted(dancing_brigade)
    return ''.join(sorted(result, key=str.lower))

# 다른 사람의 풀이
def find_children1(s):
    return ''.join(sorted(sorted(s), key=str.lower))

print(find_children("abBA"), "AaBb")
print(find_children("AaaaaZazzz"), "AaaaaaZzzz")
print(find_children("CbcBcbaA"), "AaBbbCcc")
print(find_children("xXfuUuuF"), "FfUuuuXx")
print(find_children(""), "")