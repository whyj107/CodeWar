# Find the vowels
# https://www.codewars.com/kata/5680781b6b7c2be860000036/train/python

# 나의 풀이
def vowel_indices(word):
    return [i+1 for i, w in enumerate(word) if w.lower() in 'aeiouy']

print(vowel_indices("mmm"), [])
print(vowel_indices("apple"), [1, 5])
print(vowel_indices("123456"), [])
print(vowel_indices("UNDISARMED"), [1, 4, 6, 9])