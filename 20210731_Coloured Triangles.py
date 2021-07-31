# Coloured Triangles
# https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111/train/python

# 나의 풀이
def triangle(row):
    while len(row) != 1:
        tmp = ['RGB'.replace(row[r], '').replace(row[r+1], '') if row[r] != row[r+1] else row[r] for r in range(len(row)-1)]
        row = ''.join(tmp)
    return row

print(triangle('GB'), 'R')
print(triangle('RRR'), 'R')
print(triangle('RGBG'), 'B')
print(triangle('RBRGBRB'), 'G')
print(triangle('RBRGBRBGGRRRBGBBBGG'), 'G')
print(triangle('B'), 'B')