# 6 kyu
# Detect Pangram
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

# 나의 풀이
import string
def is_pangram(s):
    alpha = list(string.ascii_lowercase)
    for _ in s:
        if _.lower() in alpha:
            alpha.remove(_.lower())
    return [] == alpha

# 다른 사람의 풀이
def is_pangram1(s):
    return set(string.lowercase) <= set(s.lower())

pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)
