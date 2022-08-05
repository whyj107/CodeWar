# Duck Shoot-Easy Version
# https://www.codewars.com/kata/57d27a0a26427672b900046f/train/python

# 나의 풀이
def duck_shoot(ammo, aim, ducks):
    tmp = list(ducks)
    for i in range(int(aim * ammo)):
        try:
            tmp[tmp.index('2')] = 'X'
        except:
            continue
    return ''.join(tmp)

def duck_shoot1(ammo, aim, ducks):
    return ducks.replace('2', 'X', int(ammo * aim))

print(duck_shoot(4, 0.64, '|~~2~~~22~2~~22~2~~~~2~~~|'), '|~~X~~~X2~2~~22~2~~~~2~~~|')
print(duck_shoot(9, 0.22, '|~~~~~~~2~2~~~|'), '|~~~~~~~X~2~~~|')
print(duck_shoot(6, 0.41, '|~~~~~22~2~~~~~|'), '|~~~~~XX~2~~~~~|')
print(duck_shoot(8, 0.05, '|2~~~~|'), '|2~~~~|')
print(duck_shoot(8, 0.05, '|~~~~~|'), '|~~~~~|')
print(duck_shoot(8, 0.92, '|~~~~2~2~~~~~22~~2~~~~2~~~2|'), '|~~~~X~X~~~~~XX~~X~~~~X~~~X|')