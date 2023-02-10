# Rock paper scissors infinite
# https://www.codewars.com/kata/62443a1ea8fca9002346d72c/train/python

# 나의 풀이
def winner(choices, p1, p2):
    l = len(choices)

    if l < 3: return 'Draw!'

    tmp = (l - 3) // 2 + 1

    p1_idx = choices.index(p1)
    p2_idx = choices.index(p2)

    p1_win = [choices[p1_idx - i] for i in range(1, tmp + 1)]
    p2_win = [choices[p2_idx - i] for i in range(1, tmp + 1)]

    if p2 in p1_win:
        return 'Player 1 won!'
    elif p1 in p2_win:
        return 'Player 2 won!'
    else:
        return 'Draw!'

# 다른 사람의 풀이
def winner(choices, p1, p2):
    d = (choices.index(p1) - choices.index(p2)) % len(choices)
    m = len(choices) / 2
    return 'Player 1 won!' if 0 < d < m else 'Player 2 won!' if m < d else 'Draw!'

winner([], '', '')