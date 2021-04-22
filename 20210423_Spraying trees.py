# Spraying trees
# https://www.codewars.com/kata/5981a139f5471fd1b2000071/train/python

# 나의 풀이
def task(w, n, c):
    worker = {'Monday': 'James', 'Tuesday': 'John', 'Wednesday': 'Robert', 'Thursday': 'Michael', 'Friday': 'William'}
    return f'It is {w} today, {worker[w]}, you have to work, you must spray {n} trees and you need {n*c} dollars to buy liquid'

print(task('Wednesday', 10, 2))
print(task('Monday', 4, 3))
print(task('Friday', 5, 4))
print(task('Tuesday', 6, 1))
print(task('Thursday', 5, 3))