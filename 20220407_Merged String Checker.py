# Merged String Checker
# https://www.codewars.com/kata/54c9fcad28ec4c6e680011aa/train/python

# 풀이
def is_merge(s, part1, part2):
    queue = [(s, part1, part2)]
    while queue:
        str, p1, p2 = queue.pop()
        if str:
            if p1 and str[0] == p1[0]:
                queue.append((str[1:], p1[1:], p2))
            if p2 and str[0] == p2[0]:
                queue.append((str[1:], p1, p2[1:]))
        else:
            if not p1 and not p2:
                return True
    return False

# print(is_merge('codewars', 'code', 'wars'))
# print(is_merge('codewars', 'cdw', 'oears'))
print(is_merge('Bananas from Bahamas', 'Bahas', 'Bananas from am'))
# print(not is_merge('codewars', 'cod', 'wars'))