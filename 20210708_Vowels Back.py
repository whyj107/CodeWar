# Vowels Back
# https://www.codewars.com/kata/57cfd92c05c1864df2001563/train/python

# 나의 풀이
def vowel_back(st):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    text = {'c': -1, 'o': -1, 'd': -3, 'e': -4}
    result = ""
    for s in st:
        n = text[s] if s in text else (9 if not s in 'aeiou' else -5)
        idx = (alpha.index(s)+n)%len(alpha)
        result += s if alpha[idx] in text else alpha[idx]
    return result

# 다른 사람의 풀이
def vowel_back1(st):
    return st.translate(str.maketrans("abcdefghijklmnopqrstuvwxyz", "vkbaafpqistuvwnyzabtpvfghi"))

print(vowel_back("testcase"), "tabtbvba")
print(vowel_back("codewars"), "bnaafvab")
print(vowel_back("exampletesthere"), "agvvyuatabtqaaa")