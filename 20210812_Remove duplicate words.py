# Remove duplicate words
# https://www.codewars.com/kata/5b39e3772ae7545f650000fc/train/python

# 나의 풀이
def remove_duplicate_words(s):
    result = []
    for i in s.split(' '):
        if not i in result:
            result.append(i)
    return ' '.join(result)

# 다른 사람의 풀이
def remove_duplicate_words1(s):
    return ' '.join(dict.fromkeys(s.split()))

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"), "alpha beta gamma delta")
print(remove_duplicate_words("my cat is my cat fat"), "my cat is fat")
