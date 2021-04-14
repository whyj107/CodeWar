# Isograms
# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

# 나의 풀이
def is_isogram(string):
    for s in string.lower():
        if string.lower().count(s) > 1:
            return False
    return True

# 다른 사람의 풀이
def is_isogram1(string):
    return len(string) == len(set(string.lower()))

print(is_isogram("Dermatoglyphics"), True )
print(is_isogram("isogram"), True )
print(is_isogram("aba"), False)
print(is_isogram("moOse"), False)
print(is_isogram("isIsogram"), False)
print(is_isogram(""), True)