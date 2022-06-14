# Sum of a sequence
# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

# 나의 풀이
def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number+1, step)])

# 다른 사람의 풀이
def f(b, e, s):
    return sum(range(b, e+1, s))

print(sequence_sum(2, 6, 2), 12)
print(sequence_sum(1, 5, 1), 15)
print(sequence_sum(1, 5, 3), 5)
print(sequence_sum(0, 15, 3), 45)
print(sequence_sum(16, 15, 3), 0)
print(sequence_sum(2, 24, 22), 26)
print(sequence_sum(2, 2, 2), 2)
print(sequence_sum(2, 2, 1), 2)
print(sequence_sum(1, 15, 3), 35)
print(sequence_sum(15, 1, 3), 0)
