# Triangle area.
# https://www.codewars.com/kata/59bd84b8a0640e7c49002398/train/python

# 나의 풀이
def t_area(t_str):
    return pow(t_str.count('\n')-2, 2)*0.5

# 다른 사람의 풀이
def t_area1(t):
    return t.count(' ') - (t.count('\n') - 2) / 2

print(t_area('\n.\n. .\n'), .5)
print(t_area('\n.\n. .\n. . .\n. . . .\n. . . . .\n'), 8.0)
print(t_area('\n.\n. .\n. . .\n'), 2.0)
print(t_area(
            '\n.\n. .\n. . .\n. . . .\n. . . . .\n. . . . . .\n. . . . . . .\n. . . . . . . .\n. . . . . . . . .\n'),
            32.0)
