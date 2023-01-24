# The 'spiraling' box
# https://www.codewars.com/kata/63b84f54693cb10065687ae5/train/python

# 풀이 : 어렵네...
def create_box(m, n):
    res = []
    for y in range(1, n + 1):
        res.append([])
        for x in range(1, m + 1):
            res[-1].append(min(x, y, m - x + 1, n - y + 1))
    return res

def create_box1(m, n):
    lst = []
    for y in range(n):
        lst.append([min([y+1, x+1, n-y, m-x]) for x in range(m)])
    return lst

print(create_box(7, 8), [[1, 1, 1, 1, 1, 1, 1],
                         [1, 2, 2, 2, 2, 2, 1],
                         [1, 2, 3, 3, 3, 2, 1],
                         [1, 2, 3, 4, 3, 2, 1],
                         [1, 2, 3, 4, 3, 2, 1],
                         [1, 2, 3, 3, 3, 2, 1],
                         [1, 2, 2, 2, 2, 2, 1],
                         [1, 1, 1, 1, 1, 1, 1]])

print(create_box(6, 4), [[1, 1, 1, 1, 1, 1],
                         [1, 2, 2, 2, 2, 1],
                         [1, 2, 2, 2, 2, 1],
                         [1, 1, 1, 1, 1, 1]])
