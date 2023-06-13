# Alternate case
# https://www.codewars.com/kata/57a62154cf1fa5b25200031e/train/python

# 나의 풀이
def alternate_case(s):
    return ''.join(i.lower() if i.isupper() else i.upper() for i in s )

# 다른 사람의 풀이...
def alternateCase1(s):
    return s.swapcase()

print(alternate_case("ABC"), "abc")
print(alternate_case(""), "")
print(alternate_case(" "), " ")
print(alternate_case("Hello World"), "hELLO wORLD")
print(alternate_case("cODEwARS"), "CodeWars")
print(alternate_case("i LIKE MAKING KATAS VERY MUCH"), "I like making katas very much")
