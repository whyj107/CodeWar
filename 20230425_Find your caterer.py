# Find your caterer
# https://www.codewars.com/kata/6402205dca1e64004b22b8de/train/python

# 나의 풀이
# 1인당 $15
# 1인당 $20
# 1인당 $30 : 60명보다 많으면 20% 할인
def find_caterer(budget, people):
    if budget < people*15 or people==0: return -1
    if budget >= people*30 or (people>60 and budget >= people*24):
        return 3
    elif budget >= people*20:
        return 2
    elif budget >= people*15:
        return 1

# 다른 사람의 풀이
def find_caterer1(budget, people):
    if people != 0:
        pp = budget / people
        if pp < 15:
            return -1
        elif pp < 20:
            return 1
        elif pp < 24 or (pp < 30 and people <= 60):
            return 2
        else:
            return 3
    return -1

print(find_caterer(150, 10), 1)
print(find_caterer(1500, 60), 2)
print(find_caterer(1500, 61), 3)
print(find_caterer(100, 0), -1)
print(find_caterer(200, 5), 3)
print(find_caterer(1000, 45), 2)
print(find_caterer(940, 70), -1)