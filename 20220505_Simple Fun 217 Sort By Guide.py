# Simple FUn 217:Sort By Guide
# https://www.codewars.com/kata/590148d79097384be600001e/train/python

# 나의 풀이
def sort_by_guide(arr, guide):
    tmp = sorted([(i, j) for i, j in zip(guide, arr) if i != -1])
    result = []
    idx = 0
    for i in range(len(arr)):
        if guide[i] == -1:
            result.append(arr[i])
        else:
            result.append(tmp[idx][1])
            idx += 1
    return

# 다른 사람의 풀이
def sort_by_guide1(arr, guide):
    it = iter(sorted((y,x) for x,y in zip(arr, guide) if y > 0))
    return [next(it)[1] if y>0 else x for x,y in zip(arr, guide)]

print(sort_by_guide([56, 78, 3, 45, 4, 66, 2, 2, 4],
                    [3, 1, -1, -1, 2, -1, 4, -1, 5]),
                    [78, 4, 3, 45, 56, 66, 2, 2, 4])
print(sort_by_guide([45, 56, 78],
                    [-1, 2, 1]),
                    [45, 78, 56])
print(sort_by_guide([2, 5, 3, 1, 4, 70, 8],
                    [2, 5, 1, 3, -1, 4, -1]),
                    [3, 2, 1, 70, 4, 5, 8])
print(sort_by_guide([700, 800, 400, 100, 900, 325],
                    [2, -1, 1, -1, 3, -1]),
                    [400, 800, 700, 100, 900, 325])
print(sort_by_guide([70, 10, 15, 800, 400, 4, 225, 438, 509, 1000],
                    [6, 1, 4, -1, -1, 2, -1, -1, 5, 3]),
                    [10, 4, 1000, 800, 400, 15, 225, 438, 509, 70])
print(sort_by_guide([27, 67, 80, 38, 21],
                    [2, 5, 3, 1, 4]),
                    [38, 27, 80, 21, 67])
print(sort_by_guide([20], [-1]), [20])