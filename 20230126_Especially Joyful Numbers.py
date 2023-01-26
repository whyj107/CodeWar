# Especially Joyful Numbers
# https://www.codewars.com/kata/570523c146edc287a50014b1/train/python

# 나의 풀이
def number_joy(n):
    s = sum(list(map(int, str(n))))
    return n == (s*int(str(s)[::-1]))

print(number_joy(1997), False)
print(number_joy(1998), False)
print(number_joy(1729), True)
print(number_joy(18), False)