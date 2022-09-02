# Simple Fun #52: Pair Of SHoes
# https://www.codewars.com/kata/58885a7bf06a3d466e0000e3/train/python

# 나의 풀이
def pair_of_shoes(shoes):
    pairs = {}
    for s in shoes:
        if s[1] in pairs.keys():
            if s[0] not in pairs[s[1]]:
                pairs[s[1]].remove({1: 0, 0: 1}[s[0]])
                if pairs[s[1]] == []:
                    del pairs[s[1]]
            else:
                pairs[s[1]].append(s[0])
        else:
            pairs[s[1]] = [s[0]]
    return pairs == {}

# 다른 사람의 풀이
def pair_of_shoes1(shoes):
    right = sorted([j for i, j in shoes if i == 0])
    left = sorted([j for i, j in shoes if i == 1])
    return right == left

print(pair_of_shoes([[0, 21], [1, 23], [1, 21], [0, 23]]), True)
print(pair_of_shoes([[0, 21], [1, 23], [1, 21], [1, 23]]), False)
print(pair_of_shoes([[0, 23], [1, 21], [1, 23], [0, 21], [1, 22], [0, 22]]), True)
print(pair_of_shoes([[0, 23], [1, 21], [1, 23], [0, 21]]), True)
print(pair_of_shoes([[0, 23], [1, 21], [1, 22], [0, 21]]), False)
print(pair_of_shoes([[0, 23]]), False)
print(pair_of_shoes([[0, 23], [1, 23]]), True)
print(pair_of_shoes([[0, 23], [1, 23], [1, 23], [0, 23]]), True)
print(pair_of_shoes([[0, 23], [1, 22]]), False)
print(pair_of_shoes([[0, 23], [1, 23], [1, 23], [0, 23], [0, 23], [0, 23]]), False)
print(pair_of_shoes([[1, 31], [0, 44], [0, 31], [0, 31], [0, 31], [1, 31], [1, 44], [1, 31]]), True)