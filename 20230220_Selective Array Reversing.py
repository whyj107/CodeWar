# Selective Array Reversing
# https://www.codewars.com/kata/58f6000bc0ec6451960000fd/train/python

# 나의 풀이
def sel_reverse(arr, l):
    if l == 0: return arr
    result = []
    for i in range(0, len(arr), l):
        result += arr[i:i+l][::-1]
    return

# 다른 사람의 풀이
def sel_reverse1(arr,l):
    return [ elt for i in range(0, len(arr), l) for elt in arr[i:i+l][::-1] ] if l != 0 else arr

print(sel_reverse([2,4,6,8,10,12,14,16], 3), [6,4,2, 12,10,8, 16,14])
print(sel_reverse([2,4,6,8,10,12,14,16], 2), [4,2, 8,6, 12,10, 16,14])
print(sel_reverse([1,2,3,4,5,6], 2), [2,1, 4,3, 6,5])
print(sel_reverse([1,2,3,4,5,6], 0), [1,2,3,4,5,6])
print(sel_reverse([1,2,3,4,5,6], 10), [6,5,4,3,2,1])