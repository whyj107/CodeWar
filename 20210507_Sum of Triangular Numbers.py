# Sum of Triangular Numbers
# https://www.codewars.com/kata/580878d5d27b84b64c000b51/train/python

# 나의 풀이
def sum_triangular_numbers(n):
    sum_ = []
    for i in range(1, n+1):
        sum_.append(sum_[-1]+i if len(sum_) > 0 else i)
    return sum(sum_)

# 다른 사람의 풀이
def sum_triangular_numbers1(n):
    return n * (n + 1) * (n + 2) / 6 if n > 0 else 0

print(sum_triangular_numbers(6), 56)
print(sum_triangular_numbers(34), 7140)
print(sum_triangular_numbers(-291), 0)
print(sum_triangular_numbers(943), 140205240)
print(sum_triangular_numbers(-971), 0)


