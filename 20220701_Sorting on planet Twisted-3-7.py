# Sorting on planet Twisted-3-7
# https://www.codewars.com/kata/58068479c27998b11900056e/train/python

# My Solution
def sort_twisted37(arr):
    result = []
    for a in arr:
        str_a = str(a)
        if '3' in str_a or '7' in str_a:
            tmp = str_a.translate(str_a.maketrans("37", "73"))
            result.append((int(tmp), a))
        else:
            result.append((a, a))
    result = sorted(result)
    return [j for i, j in result]

# 다른 사람의 풀이
def sort_twisted37_1(arr):
    def key(x):
        return int(str(x).translate(str.maketrans('37', '73')))
    return sorted(arr, key=key)

tr=str.maketrans('37','73')
def sort_twisted37_2(arr):
    return sorted(arr,key=lambda n:int(str(n).translate(tr)))

print(sort_twisted37([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 7, 4, 5, 6, 3, 8, 9])
print(sort_twisted37([12, 13, 14]), [12, 14, 13])
print(sort_twisted37([9, 2, 4, 7, 3]), [2, 7, 4, 3, 9])
print(sort_twisted37([37, 73]), [73, 37])

