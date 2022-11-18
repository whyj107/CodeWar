# Spiral Column Addition
# https://www.codewars.com/kata/5d95118fdb5c3c0001a55c9b/train/python

# 나의 풀이 : Time Out
def spiral_column(n, c):
    arr = [[0]*n]*n
    arr[0] = [i for i in range(1, n+1)]
    start, end = 1, n
    index, num = 0, n
    for i in range(1, 2*n-1):
        arr = list(map(list, zip(*arr)))[::-1]
        for j in range(start, end):
            num += 1
            arr[index][j] = num
        if i%4 == 3: index += 1
        elif i%4 == 0: start += 1
        elif i%4 == 2: end -= 1

    for i in range(2*n-2):
        arr = list(map(list, zip(*arr)))[::-1]
    return [sum(i) for i in zip(*arr)][c-1]

# 다른 사람의 풀이
def spiral_column1(n, c):
    n2, n3, c2, c3 = n**2, n**3, c**2, c**3
    nc, nc2, n2c = n*c, n*c2, n2*c
    if 2*c <= n:
        return (24*n2c - 3*n2 - 48*nc2 + 6*nc + 3*n + 32*c3 - 6*c2 - 2*c) // 6
    return (8*n3 - 24*n2c + 9*n2 + 48*nc2 - 42*nc + 7*n - 32*c3 + 42*c2 - 10*c) // 6

def spiral_column2(n,c):
    s = 0
    while True:
        if c == n:
            return s + sum(range(n, 2 * n))
        if c == 1:
            return s + 1 + sum(range(3*n-2, 4*n-3))
        s += 4*n*n - 9*n + 7
        c -= 1
        n -= 2

print(spiral_column(1, 1), 1)
print(spiral_column(4, 1), 34)
print(spiral_column(4, 2), 40)
print(spiral_column(4, 3), 40)
print(spiral_column(4, 4), 22)
for i in range(1, 5+1):
    print(spiral_column(5, i))
print(spiral_column(6, 6))
