# Merge overlapping strings
# https://www.codewars.com/kata/61c78b57ee4be50035d28d42/train/python

# 나는 풀이
def merge_strings(first, second):
    for i in range(len(first)):
        if second.startswith(first[i:]):
            return first[:i] + second
    return first + second

sample_test_cases = [
    ('abcde', 'cdefgh', 'abcdefgh'),
    ('abaab', 'aabab', 'abaabab'),
    ('abcde', 'efghi', 'abcdefghi')
]

for first, second, expected in sample_test_cases:
    print(merge_strings(first, second), expected)