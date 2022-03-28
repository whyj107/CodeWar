# Digits explosion
# https://www.codewars.com/kata/585b1fafe08bae9988000314/train/python

# 나의 풀이
def explode(s):
    return ''.join([i*int(i) for i in s])

print(explode("312"), "333122")
print(explode("102269"),"12222666666999999999")
print(explode("0"), "")
print(explode("000"), "")
print(explode("123"), "122333")