# Which are in?
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

# 나의 풀이
def in_array(array1, array2):
    return sorted(list(set(a1 for a2 in array2 for a1 in array1 if a2.find(a1) > -1)))

def testing(array1, array2, expect):
    actual = in_array(array1, array2)
    print(actual, expect)

# 다른 사람의 풀이
def in_array1(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})

a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
testing(a1, a2, r)

a1 = ["arp", "mice", "bull"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp']
testing(a1, a2, r)