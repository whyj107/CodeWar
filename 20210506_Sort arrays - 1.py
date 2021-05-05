# Sort arrays - 1
# https://www.codewars.com/kata/51f41b98e8f176e70d0002a8/train/python

# 나의 풀이
def sortme(names):
    return sorted(names)

# 다른 사람의 풀이
sortme1=lambda x:sorted(x)

print(sortme(["one", "two", "three"]), ["one", "three", "two"])
