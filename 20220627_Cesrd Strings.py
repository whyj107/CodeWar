# Ce*s*r*d Strings
# https://www.codewars.com/kata/5ff6060ed14f4100106d8e6f/train/python

# 나의 풀이
def uncensor(infected, discovered):
    result = ''
    idx = 0
    for i in infected:
        if i == '*':
            result += discovered[idx]
            idx += 1
        else:
            result += i
    return result

# 다른 사람의 풀이
def uncensor1(infected, discovered):
    return infected.replace('*', '{}').format(*discovered)

def uncensor2(s, sub):
    it = iter(sub)
    return ''.join( c if c!='*' else next(it) for c in s )

data = [
    ('*h*s *s v*ry *tr*ng*', 'Tiiesae', 'This is very strange'),
    ('A**Z*N*', 'MAIG', 'AMAZING'),
    ('xyz', '', 'xyz'),
    ('', '', ''),
    ('***', 'abc', 'abc')
]

for infected, discovered, result in data:
    print(uncensor(infected, discovered), result)