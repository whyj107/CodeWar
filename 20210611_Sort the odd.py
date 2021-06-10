# Sort the odd
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python

# 나의 풀이
def sort_array(source_array):
    odd = sorted([i for i in source_array if i%2 != 0])
    source_array = ['odd' if i%2 != 0 else i for i in source_array]
    return [odd.pop(0) if i == 'odd' else i for i in source_array]

# 다른 사람의 풀이
def sort_array1(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]),[])