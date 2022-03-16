# Follow that Spy
# https://www.codewars.com/kata/5899a4b1a6648906fe000113/train/python

# 나의 풀이
def find_routes(routes):
    path = {i: j for i, j in routes}
    start, end = '', ''
    result = []
    for i, j in routes:
        if i not in path.values():
            start = i
        if j not in path.keys():
            end = j
    while start != end:
        result.append(start)
        start = path[start]
    result.append(end)

    return ', '.join(result)

# 다른 사람의 풀이
def find_routes1(routes):
    routes = dict(routes)
    destinations = set(routes.values())
    path = [next(place for place in routes if place not in destinations)]
    while next_place := routes.get(path[-1]):
        path.append(next_place)
    return ', '.join(path)

sample_test_cases = [
    ('Basic tests', [
        ([('one', 'two')], 'one, two'),
        ([('one', 'two'), ('two', 'three')], 'one, two, three'),
        ([('two', 'three'), ('one', 'two')], 'one, two, three'),
    ]),
]

for name, test_cases in sample_test_cases:
    for routes, expected in test_cases:
        print(find_routes(routes), expected)