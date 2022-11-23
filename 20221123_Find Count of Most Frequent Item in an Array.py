# Find Count of Most Frequent Item in an Array
# https://www.codewars.com/kata/56582133c932d8239900002e/train/python

# 나의 풀이
from collections import Counter
def most_frequent_item_count(collection):
    tmp = Counter(collection).most_common(1)
    return 0 if tmp == [] else tmp[0][1]

# 다른 사람의 풀이
def most_frequent_item_count1(collection):
    if collection:
        return max([collection.count(item) for item in collection])
    return 0

print(most_frequent_item_count([3, -1, -1]), 2)
print(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5)
print(most_frequent_item_count([]), 0)
print(most_frequent_item_count([9]), 1)