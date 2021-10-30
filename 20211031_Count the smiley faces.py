# Count the smiley faces!
# https://www.codewars.com/kata/583203e6eb35d7980400002a/train/python

# 나의 풀이
def count_smileys(arr):
    result = 0
    for a in arr:
        if a[0] in [':', ';'] and a[-1] in [')', 'D']:
            if len(a) == 3 and a[1] in ['-', '~']:
                result += 1
            elif len(a) == 2:
                result += 1
    return result

# 다른 사람의 풀이
from re import findall
def count_smileys1(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

print(count_smileys([]), 0)
print(count_smileys([':D', ':~)', ';~D', ':)']), 4)
print(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
print(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)