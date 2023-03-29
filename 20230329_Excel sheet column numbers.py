# Excel sheet column numbers
# https://www.codewars.com/kata/55ee3ebff71e82a30000006a/train/python

# 나의 풀이
def title_to_number(title):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum(pow(26, i)*(alpha.index(t)+1) for i, t in enumerate(title[::-1]))

# 다른 사람의 풀이
def title_to_number1(title):
    return sum((ord(c) - 64) * 26**i for i, c in enumerate(title[::-1]))

print(title_to_number('A'),1)
print(title_to_number('Z'),26)
print(title_to_number('AA'),27)
print(title_to_number('AZ'),52)
print(title_to_number('BA'),53)
print(title_to_number('CODEWARS'),28779382963)