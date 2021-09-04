# Fold an array
# https://www.codewars.com/kata/57ea70aa5500adfe8a000110/train/python

# 나의 풀이
def fold_array(array, runs):
    for _ in range(runs):
        result = []
        for i in range(len(array)//2):
            result.append(array[i] + array[len(array)-i-1])
        if len(array)%2 != 0:
            result.append(array[len(array)//2])
        array = result
    return array

# 다른 사람의 풀이
def fold_array1(array, runs):
    worker = array[:]
    for r in range(runs):
        for i in range(len(worker)//2):
            worker[i] += worker.pop()
    return worker

arr = [1, 2, 3, 4, 5]

tests = [
    [[arr, 1], [6, 6, 3]],
    [[arr, 2], [9, 6]],
    [[arr, 3], [15]],
    [[[-9, 9, -8, 8, 66, 23], 1], [14, 75, 0]],
]

for inp, exp in tests:
    print(fold_array(*inp), exp)