# Rule 30
# https://www.codewars.com/kata/5581e52ac76ffdea700000c1/train/python

# 나의 풀이
def rule30(list_, n):
    for _ in range(n):
        list_ = [0] + list_ + [0]
        tmp = []
        for i in range(len(list_)):
            if i == 0:
                r = 0^(list_[i]|list_[i+1])
            elif i == len(list_)-1:
                r = list_[i-1]^(list_[i]|0)
            else:
                r = list_[i-1]^(list_[i]|list_[i+1])
            tmp.append(r)
        list_ = tmp.copy()
    return list_

# 다른 사람의 풀이
def rule301(a, n):
    for _ in range(n):
        a = [int(0 < 4*x + 2*y + z < 5) for x, y, z in
                zip([0, 0] + a, [0] + a + [0], a + [0, 0])]
    return a

def rule302(arr, n):
    for _ in range(n):
        arr = [a ^ (b | c) for a, b, c in zip([0, 0, *arr], [0, *arr, 0], [*arr, 0, 0])]
    return arr

print(rule30([1], 1), [1, 1, 1])
print(rule30([1], 2), [1, 1, 0, 0, 1])