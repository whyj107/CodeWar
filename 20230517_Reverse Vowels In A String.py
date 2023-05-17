# Reverse Vowels In A String
# https://www.codewars.com/kata/585db3e8eec141ce9a00008f/train/python

# 나의 풀이
def reverse_vowels(s):
    vowels = [_ for _ in s if _ in 'aeiouAEIOU'][::-1]
    idx = 0
    result = ''
    for _ in s:
        if _ in 'aeiouAEIOU':
            result += vowels[idx]
            idx += 1
        else:
            result += _
    return result

# 다른 사람의 풀이
import re
VOWS = re.compile(r'[aeiou]', flags=re.I)
def reverse_vowels1(s):
    vows = VOWS.findall(s)
    return VOWS.sub(lambda _:vows.pop(), s)

print(reverse_vowels("Hello!"), "Holle!")
print(reverse_vowels("Tomatoes"), "Temotaos")
print(reverse_vowels("Reverse Vowels In A String"), "RivArsI Vewols en e Streng")