# Cats and shelves
# https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/python

# 나의 풀이
def solution(start, finish):
    cnt = 0
    while start < finish:
        if start + 3 <= finish:
            start += 3
        else:
            start += 1
        cnt += 1
    return cnt

# 다른 사람의 풀이
def solution1(start, finish):
    return sum(divmod(finish-start, 3))

print(solution(1, 5), 2)
print(solution(2, 4), 2)
print(solution(652, 925), 91)