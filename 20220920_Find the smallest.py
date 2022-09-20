# Find the smallest
# https://www.codewars.com/kata/573992c724fc289553000e95/train/python

# 풀이
def smallest(n):
    s = str(n)
    min1, from1, to1 = n, 0, 0
    for i in range(len(s)):
        removed = s[:i] + s[i+1:]
        for j in range(len(removed)+1):
            num = int(removed[:j] + s[i] + removed[j:])
            if num < min1:
                min1, from1, to1 = num, i, j
    return [min1, from1, to1]

print(smallest(261235), [126235, 2, 0])
print(smallest(209917), [29917, 0, 1])
print(smallest(285365), [238565, 3, 1])
print(smallest(269045), [26945, 3, 0])
print(smallest(296837), [239687, 4, 1])