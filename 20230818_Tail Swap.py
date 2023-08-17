# Tail Swap
# https://www.codewars.com/kata/5868812b15f0057e05000001/train/python

# 나의 풀이
def tail_swap(strings):
    a = strings[0].split(":")
    b = strings[-1].split(':')
    return [f'{a[0]}:{b[-1]}', f'{b[0]}:{a[-1]}']


sample_test_cases = [
    (['abc:123', 'cde:456'], ['abc:456', 'cde:123']),
    (['a:12345', '777:xyz'], ['a:xyz'  , '777:12345']),
]

for strings, expected in sample_test_cases:
    msg = f'tail_swap({strings!r})'
    print(tail_swap(strings), expected, msg)