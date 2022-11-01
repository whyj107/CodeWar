# Vowel one
# https://www.codewars.com/kata/580751a40b5a777a200000a1/train/python

# 나의 풀이
def vowel_one1(s):
    return ''.join(['1' if i.lower() in 'aeiou' else '0' for i in s])

# 다른 사람의 풀이
def vowel_one(s):
    return "".join("01"[c in "aeoui"] for c in s.lower())

tests = [
    # [input, expected],
    ["vowelOne", "01010101"],
    ["123, arou", "000001011"],
    ["Codewars", "01010100"],
    ["Python", "000010"]
]

for inp, exp in tests:
    print(vowel_one(inp), exp)