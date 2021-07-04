# Remove First and Last Character
# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/train/python

# 나의 풀이
def remove_char(s):
    return s[1:-1]

print(remove_char('eloquent'), 'loquen')
print(remove_char('country'), 'ountr')
print(remove_char('person'), 'erso')
print(remove_char('place'), 'lac')
print(remove_char('ok'), '')
print(remove_char('ooopsss'), 'oopss')
