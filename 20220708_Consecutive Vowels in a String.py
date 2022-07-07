# Consecutive Vowels in a String
# https://www.codewars.com/kata/62a933d6d6deb7001093de16/train/python

# 나의 풀이
def get_the_vowels(word):
    result = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for w in word:
        if vowel[result%5] == w:
            result += 1
    return result

string = "agrtertyfikfmroyrntbvsukldkfa"
print(get_the_vowels(string), 6, f'Correct answer for {string}')

string = "erfaiekjudhyfimngukduo"
print(get_the_vowels(string), 4, f'Correct answer for {string}')

string = "akfheujfkgiaaaofmmfkdfuaiiie"
print(get_the_vowels(string), 7, f'Correct answer for {string}')