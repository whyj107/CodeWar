# Piano Kata, Part 1
# https://www.codewars.com/kata/589273272fab865136000108/train/python

# 나의 풀이
def black_or_white_key(k):
    result = "wbwwbwbwwbwb"
    return "white" if result[(k-1) % 88 % len(result)] == 'w' else "black"

# 다른 사람의 풀이
w, b = "white", "black"
keyboard = [w, b, w, w, b, w, b, w, w, b, w, b]
def black_or_white_key1(count):
    return keyboard[(count - 1) % 88 % 12]

print(black_or_white_key(1), "white")
print(black_or_white_key(5), "black")
print(black_or_white_key(12), "black")
print(black_or_white_key(42), "white")
print(black_or_white_key(88), "white")
print(black_or_white_key(89), "white")
print(black_or_white_key(92), "white")
print(black_or_white_key(100), "black")
print(black_or_white_key(111), "white")
print(black_or_white_key(200), "black")
print(black_or_white_key(2017), "white")
