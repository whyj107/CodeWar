# Value of x
# https://www.codewars.com/kata/614ac445f13ead000f91b4d0/train/python

# 나의 풀이
def solve(eq: str):
    tmp = eq.split('=')
    if 'x' in tmp[0]:
        result = tmp[1]
        cal = tmp[0].replace(' ', '')
    else:
        result = tmp[0]
        cal = tmp[1].replace(' ', '')

    x_idx = cal.index('x')

    cal = cal.replace('x', '0')

    if cal[x_idx-1] == '-':
        t = -1
    else:
        t = 1

    result += f'-({cal})'

    return eval(result) * t

# 다른 사람의 풀이
def solve1(eq):
    a,b = eq.replace('x','0').split('=')
    x = eval(a) - eval(b)
    if '- x' in eq: x*=-1
    return x if eq.index('x') > eq.index('=') else -x

easy_cases = {
    'x + 1 = 9 - 2': 6,
    'x - 2 + 3 = 2': 1,
    'x = + 2 - 5 + 9': 6}

exceptional_cases = {
    '- 10 = x': -10,
    '- x = - 1': 1,
    'x - 0 + 0 = 0': 0}


for case, ans in easy_cases.items():
    print(solve(case), ans)

for case, ans in exceptional_cases.items():
    print(solve(case), ans)
