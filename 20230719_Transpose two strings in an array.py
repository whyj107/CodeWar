# Transpose two strings in an array
# https://www.codewars.com/kata/581f4ac139dc423f04000b99/train/python

# 나의 풀이
def transpose_two_strings(arr):
    m = max(len(arr[0]), len(arr[1]))
    arr[0] = arr[0].ljust(m, ' ')
    arr[1] = arr[1].ljust(m, ' ')
    return '\n'.join([f'{arr[0][i]} {arr[1][i]}' for i in range(m)])

# 다른 사람의 풀이
from itertools import zip_longest
def transpose_two_strings1(lst):
    return "\n".join(f"{a} {b}" for a, b in zip_longest(*lst, fillvalue=" "))



print(transpose_two_strings(["Hello", "World"]), "H W\ne o\nl r\nl l\no d")
print(transpose_two_strings(["joey", "louise"]), "j l\no o\ne u\ny i\n  s\n  e")
print(transpose_two_strings(["a", "cat"]), "a c\n  a\n  t")
print(transpose_two_strings(["cat", ""]), "c  \na  \nt  ")
print(transpose_two_strings(["!a!a!", "?b?b"]), "! ?\na b\n! ?\na b\n!  ")