# Triple Crown
# https://www.codewars.com/kata/61e173ccbc916700267ef2ae/train/python

# 나의 풀이
def triple_crown(receivers):
    ry, rt, r = 0, 0, 0
    result = ['', '', '']
    for k, v in receivers.items():
        if ry < v['Receiving yards']:
            result[0] = k
            ry = v['Receiving yards']
        elif ry == v['Receiving yards']:
            result[0] = ''
        if rt < v['Receiving touchdowns']:
            result[1] = k
            rt = v['Receiving touchdowns']
        elif rt == v['Receiving touchdowns']:
            result[1] = ''
        if r < v['Receptions']:
            result[2] = k
            r = v['Receptions']
        elif r == v['Receptions']:
            result[2] = ''
    return result[0] if result[0] == result[1] and result[0] == result[2] else 'None of them'

# 다른 사람의 풀이
def triple_crown1(r):
    for i in r:
        if all(r[i][k]>r[j][k] for k in r[i] for j in r if i!=j):
            return i
    return 'None of them'

print(triple_crown({'Cooper Kupp': {'Receiving yards': 1800, 'Receiving touchdowns': 18, 'Receptions': 117},
                    'Justin Jefferson': {'Receiving yards': 1700, 'Receiving touchdowns': 17, 'Receptions': 116},
                    'Davante Adams': {'Receiving yards': 1750, 'Receiving touchdowns': 16, 'Receptions': 113}}), 'Cooper Kupp')
print(triple_crown({'Cooper Kupp': {'Receiving yards': 1700, 'Receiving touchdowns': 18, 'Receptions': 117},
                    'Justin Jefferson': {'Receiving yards':1650, 'Receiving touchdowns': 17, 'Receptions': 115},
                    'Davante Adams': {'Receiving yards': 1750, 'Receiving touchdowns': 16, 'Receptions': 113}}), 'None of them')
print(triple_crown({'Cooper Kupp': {'Receiving yards': 1800, 'Receiving touchdowns': 16, 'Receptions': 110},
                    'Justin Jefferson': {'Receiving yards': 1725, 'Receiving touchdowns': 15, 'Receptions': 112},
                    'Davante Adams': {'Receiving yards': 1800, 'Receiving touchdowns': 16, 'Receptions': 113}}), 'None of them')
print(triple_crown({'Cooper Kupp': {'Receiving yards': 1587, 'Receiving touchdowns': 11, 'Receptions': 106},
                    'Justin Jefferson': {'Receiving yards': 1760, 'Receiving touchdowns': 11, 'Receptions': 104},
                    'Davante Adams': {'Receiving yards': 1768, 'Receiving touchdowns': 20, 'Receptions': 113}}))
print(triple_crown({'Cooper Kupp': {'Receiving yards': 1791, 'Receiving touchdowns': 13, 'Receptions': 106},
                    'Justin Jefferson': {'Receiving yards': 1909, 'Receiving touchdowns': 10, 'Receptions': 110},
                    'Davante Adams': {'Receiving yards': 1802, 'Receiving touchdowns': 16, 'Receptions': 114}}))