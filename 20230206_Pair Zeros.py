# Pair Zeros
# https://www.codewars.com/kata/54e2213f13d73eb9de0006d2/train/python

# 나의 풀이
def pair_zeros(arr):
    zero = False
    result = []
    for a in arr:
        if a == 0:
            zero = not zero
            if not zero:
                continue
        result.append(a)
    return result

# 다른 사람의 풀이
def pair_zeros(arr):
    store_0 = 0
    return [v for v in arr if v or (store_0 := store_0^1)]

print(pair_zeros([]), [])
print(pair_zeros([1]), [1])
print(pair_zeros([1, 2, 3]), [1, 2, 3])
print(pair_zeros([0]), [0])
print(pair_zeros([0, 0]), [0])
print(pair_zeros([1, 0, 1, 0, 2, 0, 0]), [1, 0, 1, 2, 0])
print(pair_zeros([0, 0, 0]), [0, 0])
print(pair_zeros([1, 0, 1, 0, 2, 0, 0, 3, 0]), [1, 0, 1, 2, 0, 3, 0])
print(pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])
print(pair_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0, 0])