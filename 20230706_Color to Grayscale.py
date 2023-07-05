# Color to Grayscale
# https://www.codewars.com/kata/649c4012aaad69003f1299c1/train/python

# 나의 풀이
def rgb_to_grayscale(color):
    result = int(color[1:3], 16)*0.299 + int(color[3:5], 16)*0.587 + int(color[5:7], 16)*0.114
    h = hex(round(result))[2:]
    return f'#{h.zfill(2)*3}'

# 다른 사람의 풀이
def rgb_to_grayscale1(color):
    return '#' + 3 * format(round(  0.299 * int(color[1:3], 16)
                                  + 0.587 * int(color[3:5], 16)
                                  + 0.114 * int(color[5:7], 16)
                                 ),
                            '02X')

def rgb_to_grayscale2(color):
    r,g,b = (int(color[i:i+2],16) for i in range(1,6,2))
    y = .299*r + .587*g + .114*b
    return '#' + f'{ round(y) :02X}'*3

print(rgb_to_grayscale("#FFFFFF").upper(), '#FFFFFF')
print(rgb_to_grayscale("#0000FF").upper(), '#1D1D1D')
print(rgb_to_grayscale("#00FF00").upper(), '#969696')
print(rgb_to_grayscale("#FF0000").upper(), '#4C4C4C')
print(rgb_to_grayscale("#000000").upper(), '#000000')