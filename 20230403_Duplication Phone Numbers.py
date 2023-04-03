# Simple Fun #186: Duplicate Phone Numbers
# https://www.codewars.com/kata/58bf67eb68d8469e3c000041/train/python

# 나의 풀이
# 2 : A, B, C    3 : D, E, F    4 : G, H, I    5 : J, K, L
# 6 : M, N, O    7 : P, R, S    8 : T, U, V    9 : W, X, Y
# Q, Z 는 없음
def find_duplicate_phone_numbers(phone_numbers):
    tmp = {'a':'2', 'b':'2', 'c':'2', 'd':'3', 'e':'3', 'f':'3',
           'g':'4', 'h':'4', 'i':'4', 'j':'5', 'k':'5', 'l':'5',
           'm':'6', 'n':'6', 'o':'6', 'p':'7', 'r':'7', 's':'7',
           't':'8', 'u':'8', 'v':'8', 'w':'9', 'x':'9', 'y':'9'}
    result = {}
    for p in phone_numbers:
        r = ''
        for _ in p:
            if _.isnumeric():
                r += _
            elif _.lower() in tmp:
                r += tmp[_.lower()]
            if len(r) == 3: r += '-'

        result.setdefault(r, 0)
        result[r] += 1
    result = dict(sorted(result.items()))
    return [f'{k}:{v}' for k, v in result.items() if v>1]

# 다른 사람의 풀이
def find_duplicate_phone_numbers1(phone_numbers):
  stan  = [a.upper().translate(str.maketrans('ABCDEFGHIJKLMNOPRSTUVWXY', '222333444555666777888999')).replace('-','') for a in phone_numbers]
  return sorted(['{}-{}:{}'.format(a[:3], a[3:], stan.count(a)) for a in set(stan) if stan.count(a)>1])

testarr = ["7399425", "SEXY-GAL", "Sexy-GAL", "sexy-gal", "SEXY-425", "S-E-X-Y-G-A-L"]
result = ["739-9425:6"]
print(find_duplicate_phone_numbers(testarr),result)


testarr = ["4873279", "ITS-EASY", "888-4567",
           "3-10-10-10", "888-GLOP", "TUT-GLOP", "967-11-11",
           "310-GINO", "F101010", "888-1200", "-4-8-7-3-2-7-9-",
           "487-3279"]
result = ["310-1010:2", "487-3279:4", "888-4567:3" ]
print(find_duplicate_phone_numbers(testarr),result)