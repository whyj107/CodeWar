# Wave Sorting
# https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/python

# 나의 풀이 : 어이 없는 문제이다....
def wave_sort(a):
    a.sort()
    for i in range(1, len(a), 2):
        a[i], a[i-1] = a[i-1], a[i]


# 다른 사람의 풀이
def wave_sort1(a):
    a.sort()
    a[::2], a[1::2] = a[-len(a)//2:], a[:-len(a)//2]

from itertools import cycle
def wave_sort2(a):
    a.sort()
    out = []
    c = cycle((-1, 0))
    while a:
        out.append(a.pop(next(c)))
    a.extend(out)


def is_wave_sorted(a):
    for i in range(0, len(a) - 1):
        if not i % 2 and a[i] < a[i+1]:
            print('--------------1', i)
            return False
        if i % 2 and a[i] > a[i+1]:
            print('--------------2')
            return False
    return True

a = [1, 2, 34, 4, 5, 5, 5, 65, 6, 65, 5454, 4]
wave_sort(a)
print(is_wave_sorted(a), "The list is not wave-sorted")