# Help your granny!
# https://www.codewars.com/kata/5536a85b6ed4ee5a78000035/train/python

# 나의 풀이 : 피타고라스 이용한 것
def tour(friends, friend_towns, home_to_town_distances):
    towns = {i: j for i, j in friend_towns}
    result, before = 0, 0

    for idx, f in enumerate(friends):
        town = towns.get(f, 0)
        now = home_to_town_distances.get(town, '_')

        if now == '_':
            continue

        result += (now**2 - before**2)**0.5
        before = now
    return int(result) + before

# 다른 사람의 풀이
def tour1(friends, friend_towns, home_to_town_distances):
    ft = dict(friend_towns)
    d = [home_to_town_distances[ft[f]] for f in friends if f in ft] + [0]
    return int(sum((abs(d[i]**2 - d[i-1]**2))**0.5 for i in range(0, len(d))))

friends1 = ["A1", "A2", "A3", "A4", "A5"]
fTowns1 = [["A1", "X1"], ["A2", "X2"], ["A3", "X3"], ["A4", "X4"]]
distTable1 = {"X1": 100.0, "X2": 200.0, "X3": 250.0, "X4": 300.0}
print(tour(friends1, fTowns1, distTable1), 889)
print(tour(['B1', 'B2'],
           [['B1', 'Y1'], ['B2', 'Y2'], ['B3', 'Y3'], ['B4', 'Y4'], ['B5', 'Y5']],
           {'Y1': 50.0, 'Y2': 70.0, 'Y3': 90.0, 'Y4': 110.0, 'Y5': 150.0}), 168)
