# Sum of Digits/Digital Root
# https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

# 나의 풀이
def digital_root(n):
    while len(str(n)) != 1:
        n = sum(map(int, [i for i in str(n)]))
    return n

# 다른 사람의 풀이
# 재귀
def digital_root1(n):
    return n if n < 10 else digital_root1(sum(map(int,str(n))))

# 수학적
def digital_root2(n):
    return n%9 or n and 9

print(digital_root(16), 7)
print(digital_root(942), 6)
print(digital_root(132189), 6)
print(digital_root(493193), 2)