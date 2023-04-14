# Remove words from the sentence
# https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python

# 나의 풀이
def remove(s):
    return ' '.join(_ for _ in s.split() if not _.count('!')==1)

print(remove('Hi!'), '')
print(remove('Hi!!!'),'Hi!!!')
print(remove('!Hi'), '')
print(remove('!Hi!'), '!Hi!')
print(remove('Hi! Hi!'), '')
print(remove('!!!Hi !!hi!!! !hi') , '!!!Hi !!hi!!!')
print(remove('!Hi! ! !Hi!'), '!Hi! !Hi!')