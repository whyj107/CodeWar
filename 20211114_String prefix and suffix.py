# String prefix and suffix
# https://www.codewars.com/kata/5ce969ab07d4b7002dcaa7a1/train/python

# 나의 풀이
def solve(st):
    result = 0
    for i in range(len(st)//2+1):
        if st[:i] == st[-i:]:
            result = len(st[:i])
    return result

# 다른 사람의 풀이
def solve1(st):
    return next((n for n in range(len(st)//2, 0, -1) if st[:n] == st[-n:]), 0)

print(solve("abcd"), 0)
print(solve("abcda"), 1)
print(solve("abcdabc"), 3)
print(solve("abcabc"), 3)
print(solve("abcabca"), 1)
print(solve("aaaaa"), 2)
print(solve("aaaa"), 2)
print(solve("aaa"), 1)
print(solve("aa"), 1)
print(solve("a"), 0)