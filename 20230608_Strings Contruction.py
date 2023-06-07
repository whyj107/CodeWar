# Simple Fun #30: Strings Construction
# https://www.codewars.com/kata/58870402c81516bbdb000088/train/python

# 나의 풀이
def strings_construction(a, b):
    return min([b.count(_)//a.count(_) for _ in a])

print(strings_construction("abc", "abccba"), 2)
print(strings_construction("hnccv", "hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"), 3)
print(strings_construction("abc", "def"), 0)
print(strings_construction("zzz", "zzzzzzzzzzz"), 3)