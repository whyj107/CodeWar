# Is the King in check?
# https://www.codewars.com/kata/5e28ae347036fa001a504bbe/train/python

# 나의 풀이
def king_is_in_check(chessboard):
    king = ()
    position = {'♛': [], '♝': [], '♞': [], '♜': [], '♟': []}
    for i, chess in enumerate(chessboard):
        for j, c in enumerate(chess):
            if c in position.keys():
                position[c].append((i, j))
            elif c == '♔':
                king = (i, j)

    # '♟'
    for p in position['♟']:
        (i, j) = p
        if i != -10 and (king in [(i+1, j-1), (i+1, j+1)]):
            return True
    # '♜'
    for p in position['♜']:
        (i, j) = p
        if i != -10 and rook(chessboard, king, i, j):
            return True
    # '♞'
    for p in position['♞']:
        (i, j) = p
        if i != -10 and (king in [(i-1, j-2), (i+1, j-2), (i-2, j-1), (i-2, j+1),
                                  (i+2, j-1), (i+2, j+1), (i-1, j+2), (i+1, j+2)]):
            return True
    # '♝'
    for p in position['♝']:
        (i, j) = p
        if i != -10 and bishop(chessboard, king, i, j):
            return True
    # '♛'
    for p in position['♛']:
        (i, j) = p
        if i != -10 and (rook(chessboard, king, i, j) or bishop(chessboard, king, i, j)):
            return True
    return False


def rook(chessboard, king, i, j):
    rook_i, rook_j = [], []
    if king[0] == i:
        rook_i = set([chessboard[i][_] for _ in range(min(king[1], j), max(king[1], j)+1) if not chessboard[i][_] == ' '])
    elif king[1] == j:
        rook_j = set([chessboard[_][j] for _ in range(min(king[0], i), max(king[0], i)+1) if not chessboard[_][j] == ' '])
    if len(rook_i) == 2 or len(rook_j) == 2:
        return True
    else:
        return False

def bishop(chessboard, king, i, j):
    bishop_i = -1 if king[0] < i else 1
    bishop_j = -1 if king[1] < j else 1
    result = set([])
    while i != king[0] and j != king[1]:
        i += bishop_i
        j += bishop_j
        if chessboard[i][j] != ' ':
            result.add(chessboard[i][j])
    return result == {'♔'}


# 다른 사람의 풀이
MOVES = {
    '♜': [[x*m for m in range(1,9)] for x in (-1,-1j,1,1j)],
    '♝': [[x*m for m in range(1,9)] for x in (-1-1j,-1+1j,1-1j,1+1j)],
    '♞': [[x+1j*m] for m in range(-2,3) for x in range(-2,3) if abs(x*m) == 2],
    '♟': [[1-1j], [1+1j]],
}
MOVES['♛'] = MOVES['♜'] + MOVES['♝']
def king_is_in_check1(chessboard):
    pieces = {x + 1j * y: piece for x, row in enumerate(chessboard)
              for y, piece in enumerate(row) if piece != ' '}
    for z, piece in pieces.items():
        for it in MOVES.get(piece, ()):
            for dz in it:
                if z+dz in pieces:
                    if pieces.get(z+dz) == '♔':
                        return True
                    break
    return False

cases = iter([
    {
        "description": "Should work with a check by pawn",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♟',' ',' ',' ',' '],
            [' ',' ','♔',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": True
    },
    {
        "description": "Should work with a check by bishop",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ','♝'],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♔',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": True
    },
    {
        "description": "Should work with a check by rook",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ','♔',' ',' ','♜',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": True
    },
    {
        "description": "Should work with a check by knight",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ','♔',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♞',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": True
    },
    {
        "description": "Should work with a check by queen",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ','♛',' ','♔',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": True
    },
    {
        "description": "Should work with a king alone",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ','♔',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": False
    },
    {
        "description": "Should work with no check",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♛',' ',' ','♞',' ',' ',' ','♛'],
            [' ',' ',' ','♔',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": False
    },
    {
        "description": "Should work with a piece blocking another's line of sight",
        "board": [
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            ['♜',' ','♝','♔',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' ']
        ],
        "expected": False
    }
])

"""
for case in cases:
    chessboard = case["board"]
    print(king_is_in_check(chessboard), case["expected"])

print(king_is_in_check(
    [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', '♛', ' ', ' ', ' ', ' ', ' ', '♛'],
     [' ', '♝', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', '♝', ' ', ' ', ' ', ' '],
     ['♔', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
     [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]), False)
"""

print(king_is_in_check([
    [' ', ' ', ' ', '♟', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '♟', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', '♔', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]), False)