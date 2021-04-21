# Evens times last
# https://www.codewars.com/kata/5a1a9e5032b8b98477000004/train/python

# 나의 풀이
def even_last(numbers):
    return sum(numbers[n] for n in range(0, len(numbers), 2)) * numbers[-1] if len(numbers) > 0 else 0

# 다른 사람의 풀이
def even_last1(numbers):
    return sum(numbers[::2]) * numbers[-1] if numbers else 0

print(even_last([2, 3, 4, 5]), 30)
print(even_last([]), 0)