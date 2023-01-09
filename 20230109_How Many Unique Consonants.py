# How Many Unique Consonants?
# https://www.codewars.com/kata/5a19226646d843de9000007d/train/python

# 나의 풀이
def count_consonants(text):
    return sum(1 for t in set(text.lower()) if (t not in 'aeiou') and t.isalpha())

# 다름 사람의 풀이
def count_consonants1(s):
    return len({c for c in s.lower() if c in 'bcdfghjklmnpqrstvwxyz'})

print(count_consonants('sillystring'), 7)
print(count_consonants('aeiou'), 0)
print(count_consonants('abcdefghijklmnopqrstuvwxyz'), 21)
print(count_consonants('Count my unique consonants!!'), 7)