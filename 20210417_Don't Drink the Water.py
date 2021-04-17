# Don't Drink the Water
# https://www.codewars.com/kata/562e6df5cf2d3908ad00019e/train/python

# 나의 풀이
def separate_liquids(glass):
    result, tmp1, tmp2 = [], [], []
    length = 0
    dic = {'O': 0, 'A': 1, 'W': 2, 'H': 3}
    for g1 in glass:
        length = len(g1)
        for g2 in g1:
            tmp1.append((dic[g2], g2))
    tmp1.sort()
    idx = 0
    for i, j in tmp1:
        tmp2.append(j)
        idx += 1
        if idx % length == 0 and idx != 0:
            result.append(tmp2)
            tmp2 = []
    return result

# 다른 사람의 풀이
def separate_liquids1(g):
    s = sorted(sum(g, []), key="OAWH".index)
    return map(list, zip(*[iter(s)]*len(g and g[0])))


print(separate_liquids([['H', 'H', 'W', 'O'], ['W', 'W', 'O', 'W'], ['H', 'H', 'O', 'O']]),
                       [['O', 'O', 'O', 'O'], ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']])
print(separate_liquids([['A', 'A', 'O', 'H'], ['A', 'H', 'W', 'O'], ['W', 'W', 'A', 'W'], ['H', 'H', 'O', 'O']]),
                       [['O', 'O', 'O', 'O'], ['A', 'A', 'A', 'A'], ['W', 'W', 'W', 'W'], ['H', 'H', 'H', 'H']])

print(separate_liquids([['A', 'H', 'W', 'O']]), [['O', 'A', 'W', 'H']])
print(separate_liquids([['A'], ['H'], ['W'], ['O']]), [['O'], ['A'], ['W'], ['H']])
print(separate_liquids([]), [],)