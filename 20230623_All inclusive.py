# All Inclusive?
# https://www.codewars.com/kata/5700c9acc1555755be00027e/train/python

# 나의 풀이
def contain_all_rots(strng, arr):
    if strng=="": return True
    return all([strng[i:]+strng[:i] in arr for i in range(len(strng))])

print(contain_all_rots("", []), True)
print(contain_all_rots("", ["bsjq", "qbsj"]), True)
print(contain_all_rots("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]), True)
print(contain_all_rots("XjYABhR", ["TzYxlgfnhf", "yqVAuoLjMLy", "BhRXjYA", "YABhRXj", "hRXjYAB", "jYABhRX", "XjYABhR", "ABhRXjY"]), False)