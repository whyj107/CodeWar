# Return String of First Characters
# https://www.codewars.com/kata/5639bdcef2f9b06ce800005b/train/python

# 나의 풀이
def make_string(s):
    return ''.join(i[0] for i in s.split(' '))


print(make_string("sees eyes xray yoat"), "sexy")
print(make_string("brown eyes are nice"), "bean")
print(make_string("cars are very nice"), "cavn")
print(make_string("kaks de gan has a big head"), "kdghabh")
