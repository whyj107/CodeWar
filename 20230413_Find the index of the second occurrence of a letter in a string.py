# Find the index of the second occurrence of a letter in a string
# https://www.codewars.com/kata/63f96036b15a210058300ca9/train/python

# 나의 풀이
def second_symbol(s, symbol):
    tmp = [idx for idx, _ in enumerate(s) if _ == symbol]
    return -1 if len(tmp)<2 else tmp[1]

# 다른 사람의 풀이
def second_symbol1(s, c):
    return s.find(c, s.find(c)+1)

print(second_symbol('Hello world!!!', 'l'), 3)
print(second_symbol('Hello world!!!', 'o'), 7)
print(second_symbol('Hello world!!!', 'A'), -1)
print(second_symbol('', 'q'), -1)
print(second_symbol('Hello', '!'), -1)