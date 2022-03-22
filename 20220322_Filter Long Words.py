# Filter Long Words
# https://www.codewars.com/kata/5697fb83f41965761f000052/train/python

# 나의 풀이
def filter_long_words(sentence, n):
    return [s for s in sentence.split() if len(s) > n]

# 다른 사람의 풀이
import re
def filter_long_words1(sentence, n):
    return re.findall('[A-Za-z_\(\)]{%s,}' % str(n+1), sentence)

print(filter_long_words("The quick brown fox jumps over the lazy dog", 4), ['quick', 'brown', 'jumps'])