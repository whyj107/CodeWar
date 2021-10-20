# Return the Missing Element
# https://www.codewars.com/kata/5299413901337c637e000004/train/python

# 나의 풀이
def get_missing_element(seq):
    return list(set(range(0, 10)) - set(seq))[0]

# 다른 사람의 풀이
def get_missing_element1(seq):
    return 45 - sum(seq)

print(get_missing_element([0, 5, 1, 3, 2, 9, 7, 6, 4]), 8)
print(get_missing_element([9, 2, 4, 5, 7, 0, 8, 6, 1]), 3)