# The Office I - Outed
# https://www.codewars.com/kata/57ecf6efc7fe13eb070000e1/train/python

# 나의 풀이
def outed(meet, boss):
    a = 0
    for k, v in meet.items():
        a += 2*v if k == boss else v
    return 'Get Out Now!' if a/len(meet.keys()) <= 5 else 'Nice Work Champ!'

# 다른 사람의 풀이
def outed1(meet, boss):
    return 'Get Out Now!' if (sum(meet.values()) + meet[boss] ) / len(meet) <= 5 else 'Nice Work Champ!'

print(outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'), 'Get Out Now!')
print(outed({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9, 'mr':8}, 'katie'), 'Nice Work Champ!')
print(outed({'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2, 'mr':8}, 'john'), 'Get Out Now!')
