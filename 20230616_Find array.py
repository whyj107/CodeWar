# Find array
# https://www.codewars.com/kata/59a2a3ba5eb5d4e609000055/train/python

# 나의 풀이
def find_array(arr1, arr2):
    return [arr1[i] for i in arr2 if i < len(arr1)]

print(find_array(['a', 'a', 'a', 'a', 'a'], [2, 4]), ['a', 'a'])
print(find_array([0, 1, 5, 2, 1, 8, 9, 1, 5], [1, 4, 7]), [1, 1, 1])
print(find_array([1, 2, 3, 4, 5], [0]), [1])
print(find_array(['this', 'is', 'test'], [0, 1, 2]), ['this', 'is', 'test'])
print(find_array([0, 3, 4], [2, 6]), [4])
print(find_array([1], []), [])
print(find_array([], [2]), [])
print(find_array([], []), [])