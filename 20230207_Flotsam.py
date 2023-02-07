# Flotsam
# https://www.codewars.com/kata/635f67667dadea064acb2c4a/train/python

# 풀이 : 어려워서 못 푼 문제
def flotsam(image):
    H, W, D, S = len(image), len(image[0]), set(), next(i for i, row in enumerate(image) if '~' in row)
    def rec(i, j):
        for k,l in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
            if S <= k < H and 0 <= l < W and image[k][l] in " xFST":
                D.add(image[k][l])
                image[k][l] = '~'
                rec(k, l)
    for i,row in enumerate(image):
        for j,x in enumerate(row):
            if x == '~':
                rec(i, j)
    return ' '.join(p for p in ("Frank", "Sam", "Tom") if p[0] not in D)


pic = [
    [' ',' ', ' ',' ',' ',' ',' ',' ',' ','|','-','|',' ','|','-','|',' ','|','-','|',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ', ' ',' ',' ',' ',' ',' ',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ',' ',' ',' ',' ',' ',' ',' '],
    ['~','\\','-','-','-','-','-','-','-','|','-','|','-','|','-','|','-','|','-','|','-','-','-','-','-','-','/','~'],
    ['~','~','\\',' ',' ',' ','F',' ',' ',' ','│',' ',' ',' ','S',' ',' ',' ','│',' ',' ',' ','T',' ',' ','/','~','~'],
    ['~','~','~','\\','-','-','-','-','-','-','-','-','-','-','-','-','-','-','x','-','-','-','-','-','/','~','~','~'],
    ['~','~','~' ,'~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~'],
]
# print(flotsam(pic), "Frank Sam Tom")

pic = [
    [' ',' ', ' ',' ',' ',' ',' ',' ',' ','|','-','|',' ','|','-','|',' ','|','-','|',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ', ' ',' ',' ',' ',' ',' ',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ',' ',' ',' ',' ',' ',' ',' '],
    ['~','\\','-','-','-','-','-','-','-','|','-','|','-','|','-','|','-','|','-','|','-','-','-','-','-','-','/','~'],
    ['~','~','\\',' ',' ',' ','F',' ',' ',' ','│',' ',' ',' ','S',' ',' ',' ','│',' ',' ',' ','T',' ',' ','x','~','~'],
    ['~','~','~','\\','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','/','~','~','~'],
    ['~','~','~' ,'~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~'],
]
print(flotsam(pic), "Frank Sam")

pic = [
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ','_','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','|','_','_','_',' ',' ',' ',' ',' '],
    [' ',' ','_','_','|','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','|','_','x','x',' '],
    ['~','|',' ',' ',' ','F',' ',' ','x',' ',' ','S',' ',' ',' ',' ','|',' ',' ','T',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','/','~'],
    ['~','x','_','_','_','_','_','_','|','_','_','_','_','_','x','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','/','~','~'],
    ['~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~'],
]
print(flotsam(pic), "Tom")

pic = [
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ','_','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','|','_','_','_',' ',' ',' ',' ',' '],
    [' ',' ','_','_','|','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','|','_','x','x','x'],
    ['~','|',' ',' ',' ','F',' ',' ','x',' ',' ','S',' ',' ',' ',' ','x',' ',' ','T',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','/','~'],
    ['~','|','_','_','_','_','_','_','|','_','_','_','_','_','_','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','/','~','~'],
    ['~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~'],
]
print(flotsam(pic), "Frank Sam Tom")

pic = [
    [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ','|','=','=','|',' ',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' ','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_','_','|','_',' ',' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ','_','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','|','_','_','_',' ',' ',' ',' ',' '],
    [' ',' ','_','_','|','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','[',']','_','_','|','_','x','x',' '],
    ['~','|',' ',' ',' ','F',' ',' ','x',' ',' ','S',' ',' ',' ',' ','x',' ',' ','T',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','/','~'],
    ['~','|','x','_','_','_','_','_','|','_','_','_','_','_','_','_','|','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','/','~','~'],
    ['~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~','~'],
]
print(flotsam(pic), '')