# String repeat
# https://www.codewars.com/kata/57a0e5c372292dd76d000d7e/train/python

# 나의 풀이
def repeat_str(repeat, string):
    return string*repeat

print(repeat_str(4, 'a'), 'aaaa')
print(repeat_str(3, 'hello '), 'hello hello hello ')
print(repeat_str(2, 'abc'), 'abcabc')
