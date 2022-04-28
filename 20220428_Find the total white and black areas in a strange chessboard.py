# Find the total white and black areas in a strange chessboard
# https://www.codewars.com/kata/6262f9f7afc4729d8f5bef48/train/python

# 나의 풀이
# Time out
def white_black_areas0(cs, rs):
    white, black = 0, 0
    for idx, c in enumerate(cs):
        w = (idx%2 == 0)
        for r in rs:
            if w:
                white += (c*r)
            else:
                black += (c*r)
            w = False if w else True
    return (white, black)

def white_black_areas(cs, rs):
    white, black = 0, 0
    tmp1, tmp2 = 0, 0
    for idx, r in enumerate(rs):
        if idx%2 == 0:
            tmp1 += r
        else:
            tmp2 += r
    for idx, c in enumerate(cs):
        w = (idx%2 == 0)

        if w:
            white += (tmp1*c)
            black += (tmp2*c)
        else:
            white += (tmp2*c)
            black += (tmp1*c)
    return (white, black)

# 다른 사람의 풀이
def white_black_areas1(cs, rs):
    r_even, r_odd = sum(rs[1::2]), sum(rs[::2])
    c_even, c_odd = sum(cs[1::2]), sum(cs[::2])
    return (c_odd * r_odd + c_even * r_even, r_even * c_odd + r_odd * c_even)

print(white_black_areas([3, 1, 2, 7, 1], [1, 8, 4, 5, 2]), (146, 134))
print(white_black_areas([3, 1, 2, 7, 1, 11, 12, 3, 8, 1], [1, 8, 4, 5, 2, 21, 5, 2, 2, 17]), (1583, 1700))
print(white_black_areas([3], [2]), (6, 0))