# The fusc function -- Part 1
# https://www.codewars.com/kata/570409d3d80ec699af001bf9/train/python

# 나의 풀이
def fusc(n):
    if n < 2: return n
    if n%2 == 0: return fusc(n//2)
    else : return fusc(n//2) + fusc(n//2 + 1)

# 다른 사람의 풀이
def fusc1(n):
    assert type(n) == int and n >= 0

    if n < 2:
        return n

    if n % 2 == 0:
        return fusc1(n // 2)
    else:
        return fusc1(n // 2) + fusc1(n // 2 + 1)