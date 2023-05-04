# Closest String
# https://www.codewars.com/kata/6051151d86bab8001c83cc52/train/python

# 정해진 시간안에 풀지 못했다.
# 다른 사람의 풀이
from itertools import product
def closest_string0(lst):
    maxHamDist = lambda w: max(sum(a!=b for a,b in zip(w,s)) for s in lst)
    return min( map(''.join, product(*map(set, zip(*lst))) ), key=maxHamDist )

# 이해하기 쉬운 버전을 조금 수정했다.
from collections import Counter
def closest_string(list_str):
    counters = [Counter(i) for i in zip(*list_str)]
    minweight = len(list_str[0]) + 1
    mins = None

    # backtracking with prunning:
    def rec(s, weights):
        nonlocal minweight, mins
        if max(weights) >= minweight:
            return
        if len(s) == len(list_str[0]):
            mins = s
            minweight = max(weights)
            return

        for c in counters[len(s)].keys():
            rec(s + c, [
                prevw + (c != list_str[i][len(s)])
                for i, prevw in enumerate(weights)
            ])

    rec('', [0]*len(list_str))
    return mins

def hamming_distance(str1, str2):
    l = 0
    for i in range(0, len(str2)):
        if str1[i] != str2[i]:
            l += 1
    return l


def compare(test_case_lists, str1, str2):
    distance1 = 0
    distance2 = 0
    if type(str1) != str:
        print('You did not return a string')
    elif len(str1) != len(str2):
        print('Length of string is invalid')
    else:
        for i in test_case_lists:
            distance1 = max(hamming_distance(str1, i), distance1)
            distance2 = max(hamming_distance(str2, i), distance2)
        print(distance1, distance2, 'Your maximum hamming distance is: ' + str(
            distance1) + ' with \'' + str1 + '\'\nwhile the solution maximum is: ' + str(
            distance2) + ' with \'' + str2 + '\'\n')


l1 = ['ooi',
      'oio',
      'ooi']
us = closest_string(l1.copy())
compare(l1, us, 'ooo')
l2 = ['uvwx',
      'xuwv',
      'xvwu']
us = closest_string(l2.copy())
compare(l2, us, 'uuwu')