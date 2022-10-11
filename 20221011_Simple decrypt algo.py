# Simple decrypt algo
# https://www.codewars.com/kata/58693136b98de0e4910001ab/train/python

# 나의 풀이
def decrypt(test_key):
    result = [0]*26
    for s in test_key:
        if s.islower():
            result[ord(s)-97] += 1
    return ''.join(list(map(str, result)))

# 다른 사람으 풀이
from collections import Counter
from string import ascii_lowercase
def decrypt1(test_key):
    cnt = Counter(test_key)
    return ''.join(str(cnt[a]) for a in ascii_lowercase)

def decrypt2(key):
    return ''.join(str(key.count(c)) for c in 'abcdefghijklmnopqrstuvwxyz')

print(decrypt('$aaaa#bbb*ccfff!z'), '43200300000000000000000001')
print(decrypt('z$aaa#ccc%eee1234567890'), '30303000000000000000000001')
