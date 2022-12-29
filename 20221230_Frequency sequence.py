# Frequency sequence
# https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/python

# 나의 풀이
def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])

# 다른 사람의 풀이
from collections import Counter
def freq_seq1(s, sep):
    freq = Counter(s)
    return sep.join(str(freq[c]) for c in s)

print(freq_seq('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1')
print(freq_seq('19999999',    ':'), '1:7:7:7:7:7:7:7')
print(freq_seq('^^^**$',      'x'), '3x3x3x2x2x1')
