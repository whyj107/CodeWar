# Bumps in the Road
# https://www.codewars.com/kata/57ed30dde7728215300005fa/train/python

# 나의 풀이
def bumps(road):
    return "Car Dead" if road.count('n') > 15 else "Woohoo!"

print(bumps("n"), "Woohoo!")
print(bumps("_nnnnnnn_n__n______nn__nn_nnn"), "Car Dead")
print(bumps("______n___n_"), "Woohoo!")
print(bumps("nnnnnnnnnnnnnnnnnnnnn"), "Car Dead")