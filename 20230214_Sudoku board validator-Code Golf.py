# Sudoku board validator - Code Golf
# https://www.codewars.com/kata/63e5119516648934be4c98bd/train/python

# 이런 형식의 문제는 좋아하지 않는 편...
# 글자수 제한 150
# 풀이
validate_sudoku=lambda b:all(set(i)==set(range(1,10))for i in[[b[i//3+j//3*3][i%3+3*j%9]for i in range(9)]for j in range(9)]+b+list(zip(*b)))