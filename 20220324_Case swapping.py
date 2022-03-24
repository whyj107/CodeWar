# Case swapping
# https://www.codewars.com/kata/5590961e6620c0825000008f/train/python

# 나의 풀이
def swap(string_):
    return ''.join([s.upper() if s.islower() else s.lower() for s in string_])

# 다른 사람의 풀이
def swap1(string_):
    return string_.swapcase()

print(swap('HelloWorld'), 'hELLOwORLD')
print(swap('CodeWars'), 'cODEwARS')
print(swap('12345'), '12345')