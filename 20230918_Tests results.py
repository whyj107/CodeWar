# Test's results
# https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python

# 나의 풀이
def test(r):
    m = round(sum(r)/len(r), 3)
    dic = {'h':0, 'a':0, 'l':0}
    for i in r:
        if i > 8: dic['h'] += 1
        elif i > 6: dic['a'] += 1
        else: dic['l'] += 1
    return [m, dic, 'They did well'] if dic['a']==0 and dic['l']== 0 else [m, dic]

# 다른 사람의 풀이
from statistics import mean
def test1(r):
    dct = {'l': 0, 'a': 0, 'h': 0}
    for n in r: dct[ 'lah'[(n>6) + (n>8)] ] += 1
    return [round(mean(r), 3), dct] + ['They did well'] * (sum(dct.values()) == dct['h'])

print(test([10, 9, 9, 10, 9, 10, 9]), [9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well'])
print(test([5, 6, 4, 8, 9, 8, 9, 10, 10, 10]), [7.9, {'h': 5, 'a': 2, 'l': 3}])
print(test([5, 6, 5, 7, 4, 5, 6, 6, 5]), [5.444, {'h': 0, 'a': 1, 'l': 8}])
print(test([9, 8, 7, 6, 9, 8, 10, 7, 6]), [7.778, {'h': 3, 'a': 4, 'l': 2}])
print(test([9, 10, 10, 10, 10, 10, 8, 9, 7, 8, 10]), [9.182, {'h': 8, 'a': 3, 'l': 0}])
print(test([3, 5, 6, 10, 8, 4, 10, 9]), [6.875, {'h': 3, 'a': 1, 'l': 4}])
print(test([10, 9, 9, 10, 9, 10]), [9.5, {'h': 6, 'a': 0, 'l': 0}, 'They did well'])
print(test([7, 6, 8, 9, 6, 7, 5, 9]), [7.125, {'h': 2, 'a': 3, 'l': 3}])
print(test([9, 9, 8, 9, 8, 9]), [8.667, {'h': 4, 'a': 2, 'l': 0}])
print(test([10, 9, 6, 7, 10, 8, 9, 10]), [8.625, {'h': 5, 'a': 2, 'l': 1}])