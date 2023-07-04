# How many are smaller than me?
# https://www.codewars.com/kata/56a1c074f87bc2201200002e/train/python

# 나의 풀이
def smaller(arr):
    r = []
    for i, a in enumerate(arr):
        tmp = sum([1 for b in arr[i:] if a > b])
        r.append(tmp)
    return r

# 다른 사람의 풀이
def smaller1(arr):
    return [len([a for a in arr[i:] if a < arr[i]]) for i in range(0, len(arr))]

def smaller2(arr):
    return [sum(b < a for b in arr[i + 1:]) for i, a in enumerate(arr)]