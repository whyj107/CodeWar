# Hanoi record
# https://www.codewars.com/kata/534eb5ad704a49dcfa000ba6/train/python

# 나의 풀이
def hanoi(disks):
    return pow(2, disks) - 1

# 다른 사람의 풀이
def hanoi1(disks):
    return 2 ** disks - 1

print(hanoi(1), 1)
print(hanoi(2), 3)
print(hanoi(3), 7)
print(hanoi(5), 31)
print(hanoi(10), 1023)
print(hanoi(20), 1048575)