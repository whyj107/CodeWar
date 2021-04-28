# Map over a list of lists
# https://www.codewars.com/kata/606b43f4adea6e00425dff42/train/python

# 나의 풀이
def grid_map(inp, op):
    return [[op(j) for j in i] for i in inp]

# 다른 사람의 풀이
def grid_map1(lst, op):
    return [[*map(op,x)] for x in lst]

num_grid = [[1, 2, 3, 4], [5, 6, 7, 8, 9], [0, 2, 4]]
char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]

print(grid_map(num_grid, lambda x: x + 1), [[2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 3, 5]])
print(grid_map(num_grid, lambda x: x * 2), [[2, 4, 6, 8], [10, 12, 14, 16, 18], [0, 4, 8]])
print(grid_map(num_grid, lambda x: x ** 2), [[1, 4, 9, 16], [25, 36, 49, 64, 81], [0, 4, 16]])
print(grid_map(char_grid, lambda x: x.upper()), [['H', 'E', 'L', 'L', 'O'], ['W', 'O', 'R', 'L', 'D']])
print(grid_map(char_grid, lambda x: x.lower()), [['h', 'e', 'l', 'l', 'o'], ['w', 'o', 'r', 'l', 'd']])