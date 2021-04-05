# Max sum between two negatives
# https://www.codewars.com/kata/6066ae080168ff0032c4107a/train/python

# 다른 사람의 풀이
def max_sum_between_two_negatives(arr):
    top,c,flag = -1,0,0
    for v in arr:
        if v<0:
            if flag: top = max(top,c)
            flag,c = 1,0
        else:
            c += flag*v
    return top

print(max_sum_between_two_negatives([-1, 6, -2, 3, 5, -7]), 8)
print(max_sum_between_two_negatives([5, -1, -2]), 0)
print(max_sum_between_two_negatives([1, -2]), -1)