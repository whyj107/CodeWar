# Simple reversed parenthesis
# https://www.codewars.com/kata/5a3f2925b6cfd78fb0000040/train/python

# 나의 풀이
def solve(s):
    if len(s) % 2: return -1
    elif len(s) == 0: return 0
    s = list(map(str, s))

    cnt = 0
    if s[0] != '(':
        cnt += 1
        s[0] = '('
    if s[-1] != ')':
        cnt += 1
        s[-1] = ')'

    s = ''.join(s)
    while '()' in s:
        s = s.replace('()', '')

    cnt += solve(s)
    return cnt

# 다른 사람의 풀이
def solve1(s):
    if len(s)&1: return -1
    inv = open = 0
    for c in s:
        if c == '(':
            open += 1
        # 앞에가 '('이고 지금 ')'일 때
        elif open:
            open -= 1
        # 그냥 ')'일 때
        else:
            open = 1
            inv += 1
    return inv + open//2

print(solve(")()("), 2)
print(solve("((()"), 1)
print(solve("((("), -1)
print(solve("())((("), 3)
print(solve("())()))))()()("), 4)