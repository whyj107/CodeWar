# Simple Fun #156: Rotate Paper By 180 Degrees
# https://www.codewars.com/kata/58ad230ce0201e17080001c5/train/python

# 나의 풀이
# 뒤집어도 같은거 : 0, 2, 5, 8
# 뒤집으면 서로 바뀌는거 : 6, 9
def rotate_paper(number):
    dic = {'0':'0', '2':'2', '5':'5', '6':'9', '8':'8', '9':'6'}
    for idx, n in enumerate(number):
        if n in '1347':
            return False
        if dic[n] != number[-idx-1]:
            return False
    return True

# 다른 사람의 풀이
def rotate_paper1(number):
    return number == number.translate(str.maketrans('69', '96', '1347'))[::-1]

print(rotate_paper("000"), True)
print(rotate_paper("1"), False)
print(rotate_paper("96"), True)
print(rotate_paper("689"), True)
print(rotate_paper("56789"), False)