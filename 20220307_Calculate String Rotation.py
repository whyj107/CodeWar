# Calculate String Rotation
# https://www.codewars.com/kata/5596f6e9529e9ab6fb000014/train/python

# 나의 풀이
def shifted_diff(first, second):
    cnt = 0
    for i in range(len(first)):
        if first == second: break

        first = first[-1:] + first[:-1]
        cnt += 1

    if first != second: cnt = -1

    return cnt

# 다른 사람의 풀이
def shifted_diff1(first, second):
    return (second + second).find(first) if len(first) == len(second) else - 1;

print(shifted_diff("eecoff", "coffee"), 4)
print(shifted_diff("Moose", "moose"), -1)
print(shifted_diff("isn't", "'tisn"), 2)
print(shifted_diff("Esham", "Esham"), 0)
print(shifted_diff(" ", " "), 0)
print(shifted_diff("hoop", "pooh"), -1)
print(shifted_diff("  ", " "), -1)