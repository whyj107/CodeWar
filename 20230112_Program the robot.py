# Program the robot
# https://www.codewars.com/kata/62b0c1d358e471005d28ca7e/train/python

# 나의 풀이
def program(field, max_instructions):
    field = field.split('\n')
    (r, d) = (0, 0)
    result = []
    tmp = ''
    while d+1 != len(field) and r+1 != len(field):
        if field[d+1][r] == 'F':
            result.append(tmp + 'D')

        if field[d][r+1] == 'F':
            result.append(tmp + 'R')

        tmp = result.pop(0)

        if check(field, tmp) and len(tmp) < max_instructions+1:
            return tmp

        d = tmp.count('D')
        r = tmp.count('R')


def check(field, ins):
    i, j = 0, 0
    while i+1 < len(field) and j+1 < len(field[0]):
        for _ in ins:
            if _ == 'D':
                i += 1
            elif _ == 'R':
                j += 1

            if i == len(field) or j == len(field):
                return True
            if field[i][j] != 'F':
                return False
    return True


# 다른 사람의 풀이
from itertools import product
def program1(field, max_instructions):
    field = field.split('\n')
    last_tile = len(field) - 1

    for r in range(max_instructions):
        for p in product('RD', repeat=r + 1):  # tries all possible instructions from the shortest to the longest posssible
            p, i, finished, pos = list(p), 0, False, (0, 0)

            while True:  # Performs move until it reaches a hole or goes out of the field
                pos = (pos[0] + 1, pos[1]) if p[i % len(p)] == 'D' else (pos[0], pos[1] + 1)
                i += 1

                if max(pos) > last_tile:  # out of the field -> Finished
                    return ''.join(p)

                if field[pos[0]][pos[1]] == 'H':  # Hole -> dead, try next instruction
                    break

    return ''

print(program("FHFF\nFFHF\nFFFF\nHFFF", 2), "DR")
print(program("FHFFF\nFFHHH\nFFFFF\nHHFFF\nFFFFF", 3),"DR")
print(program("FFFFHH\nHFFFFF\nFFFFFF\nFFFFFF\nFHHFFF\nHFFFFH", 3),"RRD")
print(program("FFHFHHF\nFFFFFFF\nHFFFFFH\nFFFFFHH\nHHFFFFF\nFFFFFHF\nFFHFHFF", 3), "DRD")
print(program("FHFFHFHFFF\nFFFFHFFFFH\nFFFFFFHFFF\nFFFFFFFFFF\nFFHHFFFFFF\nFFFHFFFFFF\nHFFFFHHFFF\nFFHFFFFFFF\nFHFHHFFFFF\nFFFFHFFFFH", 4), "DRR")