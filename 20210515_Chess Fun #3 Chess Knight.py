# Chess Fun #3: Chess Knight
# https://www.codewars.com/kata/589433358420bf25950000b6/train/python

# 풀이
# 좌표를 설정해두고 풀면 될듯.
# 난 못풀어서 다른 사람 풀이를 참고했다.
def chess_knight(cell):
    i, j = " abcdefgh".index(cell[0]), int(cell[1])
    moves = [(i - 2, j - 1), (i - 2, j + 1), (i - 1, j - 2), (i - 1, j + 2),
             (i + 1, j - 2), (i + 1, j + 2), (i + 2, j - 1), (i + 2, j + 1)]
    return sum(1 for c in moves if 0 < c[0] < 9 and 0 < c[1] < 9)

moves = {(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)}
def chess_knight1(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    return sum(0 < x + mx < 9 and 0 < y + my < 9 for mx, my in moves)

print(chess_knight("a1"), 2)
print(chess_knight("c2"), 6)
print(chess_knight("d4"), 8)
print(chess_knight("g6"), 6)