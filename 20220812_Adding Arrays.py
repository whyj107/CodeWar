# Adding Arrays
# https://www.codewars.com/kata/59778cb1b061e877c50000cc/train/python

# 나의 풀이
def arr_adder(arr):
    return ' '.join([''.join(a) for a in zip(*arr)])

# 다른 사람의 풀이
def arr_adder1(arr):
    return ' '.join(map(''.join, zip(*arr)))


print(arr_adder([
    ['J', 'L', 'L', 'M'],
    ['u', 'i', 'i', 'a'],
    ['s', 'v', 'f', 'n'],
    ['t', 'e', 'e', '' ]
]), "Just Live Life Man")
print(arr_adder([
    ['T', 'M', 'i', 't', 'p', 'o', 't', 'c'],
    ['h', 'i', 's', 'h', 'o', 'f', 'h', 'e'],
    ['e', 't', '', 'e', 'w', '', 'e', 'l'],
    ['', 'o', '', '', 'e', '', '', 'l'],
    ['', 'c', '', '', 'r', '', '', ''],
    ['', 'h', '', '', 'h', '', '', ''],
    ['', 'o', '', '', 'o', '', '', ''],
    ['', 'n', '', '', 'u', '', '', ''],
    ['', 'd', '', '', 's', '', '', ''],
    ['', 'r', '', '', 'e', '', '', ''],
    ['', 'i', '', '', '', '', '', ''],
    ['', 'a', '', '', '', '', '', '']
]), "The Mitochondria is the powerhouse of the cell");
