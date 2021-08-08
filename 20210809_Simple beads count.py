# Simple beads count
# https://www.codewars.com/kata/58712dfa5c538b6fc7000569/train/python

# 나의 풀이
def count_red_beads(n):
    return (n-1)*2 if n > 1 else 0

# 다른 사람의 풀이
def count_red_beads1(nb):
    return max(0, 2 * (nb - 1) )

print(count_red_beads(1), 0)
print(count_red_beads(3), 4)
print(count_red_beads(5), 8)