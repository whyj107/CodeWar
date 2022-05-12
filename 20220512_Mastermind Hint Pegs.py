# Mastermind Hint Pegs
# https://www.codewars.com/kata/54f0d905d49112f3a300055a/train/python

# 나의 풀이
# 다른 위치, 같은 숫자 : white
# 같은 위치, 같은 숫자 : black
def get_hints(answer, guess):
    black = [1 if a == g else 0 for a, g in zip(answer, guess)]

    a_tmp = [answer[idx] for idx, b in enumerate(black) if not b]
    g_tmp = [guess[idx] for idx, b in enumerate(black) if not b]

    white = 0
    for g in g_tmp:
        if g in a_tmp:
            white += 1
            a_tmp.remove(g)

    return {"black": sum(black), "white": white}

# --------------------------------------------------
# 다른 사람의 풀이
def get_hints1(answer, guess):
    black, white = 0, 0
    for number in set(guess):
        white += min(answer.count(number), guess.count(number))

    for i, number in enumerate(guess):
        if number == answer[i]:
            white -= 1
            black += 1

    return {"black": black, "white": white}

from collections import Counter
def get_hints2(answer, guess):
    black = sum(map(int.__eq__, answer, guess))
    white = sum((Counter(answer) & Counter(guess)).values()) - black
    return {"black": black, "white": white}

print(get_hints([1, 2, 3, 4], [1, 2, 3, 4]), {"black": 4, "white": 0})
print(get_hints([1, 2, 3, 4], [4, 3, 2, 1]), {"black": 0, "white": 4})
print(get_hints([1, 2, 3, 4], [1, 1, 1, 1]), {"black": 1, "white": 0})
print(get_hints([1, 2, 3, 4], [1, 2, 4, 3]), {"black": 2, "white": 2})
print(get_hints([1, 2, 3, 4], [0, 0, 0, 0]), {"black": 0, "white": 0})