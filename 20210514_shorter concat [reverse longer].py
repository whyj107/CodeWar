# shorter concat [reverse longer]
# https://www.codewars.com/kata/54557d61126a00423b000a45/train/python

# 나의 풀이
def shorter_reverse_longer(a, b):
    if len(a) < len(b):
        a, b = b, a
    return b + a[::-1] + b

# 다른 사람의 풀이
def shorter_reverse_longer1(a,b):
    return b + a[::-1] + b if len(a) >= len(b) else a + b[::-1] + a

print(shorter_reverse_longer("first", "abcde"),"abcdetsrifabcde");
print(shorter_reverse_longer("hello", "bau"),"bauollehbau");
print(shorter_reverse_longer("abcde", "fghi"),"fghiedcbafghi");