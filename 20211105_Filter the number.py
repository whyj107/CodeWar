# Filter the number
# https://www.codewars.com/kata/55b051fac50a3292a9000025/train/python

# 나의 풀이
def filter_string(string):
    return int(''.join([s for s in string if s.isnumeric()]))

# 다른 사람의 풀이
def filter_string1(string):
    return int(filter(str.isdigit, string))

print(filter_string("123"), 123)
print(filter_string("a1b2c3"), 123)
print(filter_string("aa1bb2cc3dd"), 123)
print(filter_string("aa 112 3dd"), 1123)
print(filter_string("11bb2c23c3"), 112233)