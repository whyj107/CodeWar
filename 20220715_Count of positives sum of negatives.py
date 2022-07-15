# Count of positives / sum of negatives
# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

# 나의 풀이
def count_positives_sum_negatives(arr):
    if arr == []: return []
    result = [0, 0]
    for a in arr:
        if a > 0:
            result[0] += 1
        else:
            result[1] += a
    return result

def count_positives_sum_negatives1(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]), [10, -65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]), [8, -50])
print(count_positives_sum_negatives([1]), [1, 0])
print(count_positives_sum_negatives([-1]), [0, -1])
print(count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0])
print(count_positives_sum_negatives([]), [])