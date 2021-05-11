# Presents
# https://www.codewars.com/kata/598d6fd5b383eda05c000046/train/python

# 나의 풀이
def presents(a):
    b = [0]*len(a)
    for idx, i in enumerate(a):
        b[i-1] = idx+1
    return b

# 다른 사람의 풀이
def presents1(a):
    return [a.index(i)+1 for i in range(1,len(a)+1)]

print(presents([2, 3, 4, 1]), [4, 1, 2, 3])
print(presents([1, 3, 2]), [1, 3, 2])
print(presents([1, 2]), [1, 2])