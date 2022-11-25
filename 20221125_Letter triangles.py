# Letter triangles
# https://www.codewars.com/kata/635e70f47dadea004acb5663/train/python

# 나의 풀이
def triangle(row):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    while len(row) != 1:
        tmp = ''
        for i, j in zip(row, row[1:]):
            idx = alpha.index(i)+alpha.index(j)+1
            tmp += alpha[idx%len(alpha)]
        row = tmp
    return row


print(triangle('codewars'), 'l')
print(triangle('triangle'), 'd')
print(triangle('youhavechosentotranslatethiskata'), 'a')
print(triangle('b'), 'b')