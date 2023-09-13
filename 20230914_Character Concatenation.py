# Character Concatenation
# https://www.codewars.com/kata/55147ff29cd40b43c600058b/train/python

# 나의 풀이
def char_concat(word):
    return ''.join(word[i]+word[-i-1]+str(i+1) for i in range(len(word)//2))


print(char_concat("abc def"), 'af1be2cd3', "Should work for example test")
print(char_concat("CodeWars"), 'Cs1or2da3eW4', "Should work for 'CodeWars'")
print(char_concat("CodeWars Rocks"), 'Cs1ok2dc3eo4WR5a 6rs7',
                   "Should work for two words, like 'CodeWars Rocks'")
print(char_concat("1234567890"), '101292383474565', "Should work for numbers")
print(char_concat("$'D8KB)%PO@s"), "$s1'@2DO38P4K%5B)6", "Should work for random strings")
