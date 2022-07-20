# Get the Middle Character
# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

# 나의 풀이
def get_middle(s):
    l = len(s)
    return s[l//2-1:l//2+1] if l//2 == l/2 else s[l//2]

# 다른 사람의 풀이
def get_middle1(s):
   return s[(len(s)-1)/2:len(s)/2+1]

print(get_middle("test"), "es")
print(get_middle("testing"), "t")
print(get_middle("middle"), "dd")
print(get_middle("A"), "A")
print(get_middle("of"), "of")