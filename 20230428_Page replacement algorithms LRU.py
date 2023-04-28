# Page replacement algorithms: LRU
# https://www.codewars.com/kata/6329d94bf18e5d0e56bfca77/train/python

# 나의 풀이
def lru(n, reference_list):
    result = [-1]*n
    LRU = []
    for r in reference_list:
        if r in result:
            LRU.remove(r)
        elif -1 in result:
            idx = result.index(-1)
            result[idx] = r
        else:
            lru = LRU.pop(0)
            idx = result.index(lru)
            result[idx] = r
        LRU.append(r)
    return result

# 다른 사람의 풀이
def lru1(n, reference_list):
    cache, time = [-1] * n, [-1] * n
    for i, x in enumerate(reference_list):
        idx = cache.index(x) if x in cache else time.index(min(time))
        cache[idx] = x
        time[idx] = i
    return cache


tests = [
    [3, [1, 2, 3, 4, 3, 2, 5], [5, 2, 3]],
    [5, [], [-1, -1, -1, -1, -1]],
    [4, [5, 4, 3, 2, 3, 5, 2, 6, 7, 8], [8, 6, 7, 2]],
    [4, [1, 1, 1, 2, 2, 3], [1, 2, 3, -1]],
    [1, [5, 4, 3, 3, 4, 10], [10]],
    [3, [1, 1, 1, 1, 1, 1, 1, 1], [1, -1, -1]],
    [5, [10, 9, 8, 7, 7, 8, 7, 6, 5, 4, 3, 4, 3, 4, 5, 6, 5], [5, 4, 3, 7, 6]]
]

for t in tests:
    print(lru(t[0], t[1][:]), t[2], f"N = {t[0]}, REFERENCE LIST = {t[1]}")