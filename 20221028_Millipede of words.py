# Millipede of words
# https://www.codewars.com/kata/6344701cd748a12b99c0dbc4/train/python

# 나의 풀이 : 못 풀었음
from collections import Counter
def solution0(arr):
    start = Counter([a[0] for a in arr])
    end = Counter(a[-1] for a in arr)
    s, e = start-end, end-start
    if len(s) > 1 or len(e) > 1: return False

    return '---------------------'

# 다른 사람의 풀이
from random import shuffle
def solution1(arr):
    for _ in range(10000):
        if all(a[-1] == b[0] for a,b in zip(arr, arr[1:])):
            return True
        shuffle(arr)
    return False

from itertools import permutations as p
def solution2(a):
    return any(all(w[i][-1] == w[i+1][0] for i in range(len(a)-1)) for w in p(a))

def solution(arr):
    len_arr = len(arr)
    q = [[i] for i in range(len_arr)]
    while q != []:
        curr = q.pop(0)
        for n in range(len_arr):
            if n in curr:
                continue

            elif arr[curr[-1]][-1] == arr[n][0]:
                if len(curr) == len_arr - 1:
                    return True
                q.append(curr + [n])
    return False

print(solution(["excavate", "endure", "screen", "desire", "theater", "excess", "night"]), True)
print(solution(["trade", "pole", "view", "grave", "ladder", "mushroom", "president"]), False)
print(solution(['thesis', 'example', 'tablet', 'elephant', 'stereotype']), True)
print(solution(['cycle', 'transport', 'elite', 'empire', 'cable', 'effort']), False)
print(solution(['east', 'e', 'e', 't', 't', 'e', 'time']), True)
print(solution(['entertainment', 'cycle', 'east', 'excess', 'cable', 'exotic']), False)
print(solution(['no', 'dog', 'on', 'god']), False)