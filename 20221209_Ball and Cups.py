# Ball and Cups
# https://www.codewars.com/kata/5b715fd11db5ce5912000019/train/python

# 나의 풀이
def cup_and_balls(b, arr):
    for i in arr:
        if b in i:
            [a, c] = i
            b = c if b == a else a
    return b

#다른 사람의 풀이
def cup_and_balls(b, arr):
    for switch in arr:
        if b in switch:
            b = sum(switch) - b
    return b

print(cup_and_balls(2, [[1, 2]]), 1)
print(cup_and_balls(1, [[2, 3], [1, 2], [1, 2]]), 1)
print(cup_and_balls(2, [[1, 3], [1, 2], [2, 1], [2, 3]]), 3)
print(cup_and_balls(3, [[2, 3], [2, 1], [1, 3], [3, 1], [2, 1], [1, 2], [3, 1], [2, 3], [1, 3], [3, 1]]))
