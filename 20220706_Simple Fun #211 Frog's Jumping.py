# Simple Fun #211:Frog's Jumping
# https://www.codewars.com/kata/58fff63f4c5d026cc200000f/train/python

# My Solution
def frogs_jumping(stones):
    path = []
    i = len(stones) - 1
    print(i)
    while i > 0:
        if i > 1 and stones[i] - stones[i - 2] == 2:
            dist = jmp = 2
        else:
            dist, jmp = stones[i] - stones[i - 1], 1
        i -= jmp
        path.append(dist)
    print(path)
    return "".join(map(str, path[::-1]))

def frogs_jumping1(stones):
    c = 0
    jump = []
    for stone in stones[1:]:
        jump.append(str(stone - c))
        c = stone
    jump = "".join(jump[::-1]).replace("11", "2")
    return jump[::-1]

def frogs_jumping2(stones):
    ref, res = stones[-1], ""
    while ref:
        if ref-2 in stones:
            ref-=2
            res += '2'
        else:
            ref-=1
        res += '1'
    return res[::-1]

test_cases = (
    ([0, 1, 2, 3, 5, 6],
     '1221'),
    ([0, 2, 4, 6],
     '222'),
    ([0, 1, 2, 3],
     '12'),
    ([0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 13, 15, 16, 17],
     '122222222'),
    ([0, 2, 4, 6, 7, 8, 10, 11, 13, 15, 17, 19, 20, 21, 23],
     '222221222222'),
    ([0, 1, 2, 4, 5, 7, 9, 11, 13, 14, 15, 16, 18, 20, 21, 22, 23, 24, 26, 28, 30, 31, 32, 33, 35],
     '2212222122222222122'),
    ([0, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 30, 31, 33, 34, 36, 37, 39, 40],
     '22121212121212121212212121'),
    ([0, 1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32, 34, 35, 37, 38, 40, 41, 43, 44, 46, 47, 49],
     '22121212121212121212121212121212'),
)
for stones, expected in test_cases:
    print(frogs_jumping(stones), expected, f'stones=[{",".join(map(str,stones))}]')