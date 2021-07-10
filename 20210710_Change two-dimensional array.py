# Change two-dimensional array
# https://www.codewars.com/kata/581214d54624a8232100005f/train/python

# 나의 풀이
def matrix(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == j:
                if array[i][j] < 0:
                    array[i][j] = 0
                else:
                    array[i][j] = 1
    return array

# 다른 사람의 풀이
def matrix1(array):
    # Not mutating O(n²)
    # return [[int(x>=0) if i==j else x for j,x in enumerate(row)] for i,row in enumerate(array)]

    # Mutating O(n)
    for i in range(len(array)): array[i][i] = int(array[i][i]>=0)
    return array


print(matrix([[-1, 4, -5, -9, 3],
               [6, -4, -7, 4, -5],
               [3, 5, 4, -9, -1],
               [1, 5, -7, -8, -9],
               [-3, 2, 1, -5, 6]]) ==

               [[0, 4, -5, -9, 3],
                [6, 0, -7, 4, -5],
                [3, 5, 1, -9, -1],
                [1, 5, -7, 0, -9],
                [-3, 2, 1, -5, 1]]
               )

print(matrix([[-1, 4, -5, -9, 3],
               [6, 8, -7, 4, -5],
               [3, 5, 1, -9, -1],
               [1, 5, -7, 15, -9],
               [-3, 2, 1, -5, -6]]) ==

               [[0, 4, -5, -9, 3],
                [6, 1, -7, 4, -5],
                [3, 5, 1, -9, -1],
                [1, 5, -7, 1, -9],
                [-3, 2, 1, -5, 0]]
       )

print(matrix([[-1, 4, -5, -9, 3, 8],
               [6, 8, -7, 4, -5, -1],
               [3, 5, 1, -9, -1, 6],
               [1, 5, -7, 15, -9, 3],
               [-3, 2, 1, -5, -6, 0],
               [8, 2, 0, -2, 4, -5]]) ==

               [[0, 4, -5, -9, 3, 8],
                [6, 1, -7, 4, -5, -1],
                [3, 5, 1, -9, -1, 6],
                [1, 5, -7, 1, -9, 3],
                [-3, 2, 1, -5, 0, 0],
                [8, 2, 0, -2, 4, 0]]
                           )

print(matrix([[1, 1, -5, 5],
               [2, -4, 11, 2],
               [3, 1, -1, 4],
               [2, -6, 8, 10]]) ==

               [[1, 1, -5, 5],
                [2, 0, 11, 2],
                [3, 1, 0, 4],
                [2, -6, 8, 1]]
               )