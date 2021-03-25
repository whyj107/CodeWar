# Olympic Rings
# https://www.codewars.com/kata/57d06663eca260fe630001cc/train/python

# 나의 풀이
def olympic_ring(string):
    string = string.replace('A', 'a').replace('D', 'd').replace('O', 'o').replace('P', 'p').replace('Q', 'q')
    answer = {0: 'Not even a medal!', 1: 'Not even a medal!', 2: 'Bronze!', 3: 'Silver!'}
    answer_sum = sum(string.count(a) for a in ['a', 'B', 'b', 'd', 'e', 'g', 'o', 'p', 'q', 'R'])
    return answer.get(round((answer_sum+string.count('B'))//2), "Gold!")

# 다른 사람의 풀이
def olympic_ring1(string):
    return (['Not even a medal!'] * 2 + ['Bronze!', 'Silver!', 'Gold!'])[min(4, sum(map("abdegopqABBDOPQR".count, string)) // 2)]

print(olympic_ring('wHjMudLwtoPGocnJ'), 'Bronze!')
print(olympic_ring('eCEHWEPwwnvzMicyaRjk'), 'Bronze!')
print(olympic_ring('JKniLfLW'), 'Not even a medal!')
print(olympic_ring('EWlZlDFsEIBufsalqof'), 'Silver!')
print(olympic_ring('IMBAWejlGRTDWetPS'), 'Gold!')