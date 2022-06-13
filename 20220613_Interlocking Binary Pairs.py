# Interlocking Binary Pairs
# https://www.codewars.com/kata/628e3ee2e1daf90030239e8a/train/python

# 나의 풀이
def interlockable(a, b):
    for i, j in zip(format(a, 'b')[::-1], format(b, 'b')[::-1]):
        if i==j=='1':
            return False
    return True

# 다른 사람의 풀이
def interlockable1(a, b):
    return not a & b

for a, b, expected in ((9, 4, True),
                       (3, 6, False),
                       (2, 5, True),
                       (7, 1, False),
                       (0, 8, True)):
    a_str, b_str = str(a), str(b)
    lena, lenb = len(a_str), len(b_str)
    longer = max(lena, lenb)
    a_str = ' ' * (longer - lena) + a_str
    b_str = ' ' * (longer - lenb) + b_str

    print(interlockable(a, b), expected)