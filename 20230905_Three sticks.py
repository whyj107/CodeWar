# Three sticks
# https://www.codewars.com/kata/57c1f22d8fbb9fd88700009b/train/python

# 나의 풀이
def maxlen(L1,L2):
    min_n = min(L1, L2)
    max_n = max(L1, L2)
    if min_n < max_n/3:
        return max_n/3
    elif min_n < max_n/2:
        return min_n
    else:
        return max_n/2

# 다른 사람의 풀이
def solve(s1, s2):
    sm, lg = sorted((s1, s2))
    return min(max(lg/3, sm), lg/2)

print(maxlen(5,12),  5)
print(maxlen(12,5),  5)