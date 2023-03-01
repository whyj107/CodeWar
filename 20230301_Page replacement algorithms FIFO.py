# Page replacement algorithms: FIFO
# https://www.codewars.com/kata/62d34faad32b8c002a17d6d9/train/python

# 나의 풀이
def fifo(n, reference_list):
    result = [-1] * n
    idx = 0
    for r in reference_list:
        if r in result: continue
        result[idx%n] = r
        idx += 1
    return result

# 다른 사람의 풀이
from itertools import cycle
def fifo1(n, reference_list):
    memory = [-1] * n
    index_fifo = cycle(range(n))
    for id_page in reference_list:
        if id_page not in memory:
            memory[next(index_fifo)] = id_page
    return memory

tests = [
    [3, [1, 2, 3, 4, 2, 5], [4, 5, 3]],
    [5, [], [-1, -1, -1, -1, -1]],
    [4, [1, 2, 3, 3, 4, 5, 1], [5, 1, 3, 4]],
    [4, [1, 1, 1, 2, 2, 3], [1, 2, 3, -1]],
    [1, [5, 4, 3, 3, 4, 10], [10]],
    [3, [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1]],
    [5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5], [5, 4, 3, 7, 6]]
]

for t in tests:
    print(fifo(t[0], t[1]), t[2], f"N = {t[0]}, REFERENCE LIST = {t[1]}")

