# Bubblesort Once
# https://www.codewars.com/kata/56b97b776ffcea598a0006f2/train/python

# 나의 풀이
# Normal bubblesort
def bubblesort(l):
    end = len(l)-1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i]
                last_swap = i
        end = last_swap
    return l

def bubblesort_once(l):
    l = l[:]
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
    return l

print(bubblesort_once([9, 7, 5, 3, 1, 2, 4, 6, 8]), [7, 5, 3, 1, 2, 4, 6, 8, 9])
print(bubblesort_once([1, 3]), [1, 3])
print(bubblesort_once([3, 1]), [1, 3])
print(bubblesort_once([1, 2, 3]), [1, 2, 3])
print(bubblesort_once([2, 5, 3, 7, 1, 10, 4, 6, 8, 9]))