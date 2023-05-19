# Latin Squares
# https://www.codewars.com/kata/645fb55ecf8c290031b779ef/train/python

# 나의 풀이
# 라틴 방진
def make_latin_square(n):
    r = [i for i in range(1, n+1)]
    return [r[i:] + r[:i] for i in range(n)]

# 다른 사람의 풀이
def make_latin_square1(n):
    list = []
    for i in range(n):
        list.append([])
        for j in range(n):
            list[i].append((i+j)%n+1)
    return list