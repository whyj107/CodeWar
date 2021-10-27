# Even numbers in an array
# https://www.codewars.com/kata/5a431c0de1ce0ec33a00000c/train/python

# 나의 풀이
def even_numbers(arr, n):
    even = [a for a in arr if a%2==0]
    return even[len(even)-n:]

# 다른 사람의 풀이
def even_numbers1(arr,n):
    return [i for i in arr if i % 2 == 0][-n:]

print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 6, 8])
print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2), [-8, 26])
print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1), [6])