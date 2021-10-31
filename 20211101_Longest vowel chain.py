# Longest vowel chain
# https://www.codewars.com/kata/59c5f4e9d751df43cf000035/train/python

# 나의 풀이
def solve(s):
    tmp, result = 0, 0
    for i in s:
        if i in 'aeiou':
            tmp += 1
        else:
            result = max(tmp, result)
            tmp = 0
    return result

# 다른 사람의 풀이
def solve0(s):
    return max(map(len, ''.join(c if c in 'aeiou' else ' ' for c in s).split()))

from re import findall
def solve1(s):
    return max(map(len, findall("[aeiou]+", s)))

print(solve("codewarriors"), 2)
print(solve("suoidea"), 3)
print(solve("ultrarevolutionariees"), 3)
print(solve("strengthlessnesses"), 1)
print(solve("cuboideonavicuare"), 2)
print(solve("chrononhotonthuooaos"), 5)
print(solve("iiihoovaeaaaoougjyaw"), 8)