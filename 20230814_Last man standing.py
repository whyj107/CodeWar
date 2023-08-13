# Last man standing
# https://www.codewars.com/kata/567c26df18e9b1083a000049/train/python

# 풀이
def last_man_standing(n):
    a = list(range(1, n+1))
    while len(a)>1:
        a = a[1::2][::-1]
    return a[0]

print(last_man_standing(9), 6)
print(last_man_standing(10), 8)
print(last_man_standing(100), 54)
print(last_man_standing(1000), 510)