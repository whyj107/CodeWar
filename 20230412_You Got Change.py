# You Got Change?
# https://www.codewars.com/kata/5966f6343c0702d1dc00004c/train/python

# 나의 풀이
# 1, 5, 10, 20, 50, 100
def give_change(amount):
    tmp = [100, 50, 20, 10, 5, 1]
    result = []
    for t in tmp:
        a, b = divmod(amount, t)
        result.append(a)
        amount = b
    return tuple(result[::-1])

print(give_change(365), (0, 1, 1, 0, 1, 3))
print(give_change(217), (2, 1, 1, 0, 0, 2))