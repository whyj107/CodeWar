# Remove the minimum
# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

# 나의 풀이
def remove_smallest(numbers):
    if numbers == []: return []
    min_n  = min(numbers)
    result = []
    for i in numbers:
        if min_n == i:
            min_n = float('inf')
            continue
        result.append(i)
    return result

# 다른 사람의 풀이
def remove_smallest1(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

print(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5])
print(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4])
print(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1])
print(remove_smallest([]), [])