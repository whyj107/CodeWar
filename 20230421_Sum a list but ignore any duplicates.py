# Sum a list but ignore any duplicates
# https://www.codewars.com/kata/5993fb6c4f5d9f770c0000f2/train/python

# 나의 풀이
def sum_no_duplicates(l):
    return sum([i for i in l if l.count(i) == 1])


print(sum_no_duplicates([1, 1, 2, 3]), 5)
print(sum_no_duplicates([1, 1, 2, 2, 3]), 3)
