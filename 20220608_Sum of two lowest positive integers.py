# Sum of two lowest positive integers
# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

# 나의 풀이
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# 다른 사람의 풀이
from heapq import nsmallest
def sum_two_smallest_numbers1(numbers):
    return sum(nsmallest(2, numbers))

print(sum_two_smallest_numbers([5, 8, 12, 18, 22]), 13)
print(sum_two_smallest_numbers([7, 15, 12, 18, 22]), 19)
print(sum_two_smallest_numbers([25, 42, 12, 18, 22]), 30)