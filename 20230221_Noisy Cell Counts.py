# Noisy Cell Counts
# https://www.codewars.com/kata/63ebadc7879f2500315fa07e/train/python

# 나의 풀이
# 문제를 이해 못하겠음

# 다른 사람의 풀이
# accumulate : 누적된 합을 뽑는 것
from itertools import accumulate
def cleaned_counts(data):
    return [*accumulate(data, max)]

def cleaned_counts(data):
    new_data = data.copy()
    for i in range(1,len(new_data)):
        if new_data[i] < new_data[i-1]:
            new_data[i] = new_data[i-1]
    return new_data

"""
print(cleaned_counts([2, 1, 2]), [2, 2, 2])
print(cleaned_counts([4, 4, 4, 4]), [4, 4, 4, 4])
print(cleaned_counts([1, 1, 2, 2, 1, 2, 2, 2, 2]), [1, 1, 2, 2, 2, 2, 2, 2, 2])
print(cleaned_counts([5, 5, 6, 5, 5, 5, 5, 6]), [5, 5, 6, 6, 6, 6, 6, 6])
"""
print(cleaned_counts(
    [2, 2, 2, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 4, 5, 5, 6, 6, 7, 6, 7, 7, 7, 7, 8, 8, 8, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 10]),
    [2, 2, 2, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 4, 5, 5, 6, 6, 7, 6, 7, 7, 7, 7, 8, 8, 8, 7, 7, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 9, 10])
