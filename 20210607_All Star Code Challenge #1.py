# All Star Code Challenge #1
# https://www.codewars.com/kata/5863f97fb3a675d9a700003f/train/python

# 나의 풀이
def sum_ppg(playerOne, playerTwo):
    return playerOne['ppg'] + playerTwo['ppg']

# 다른 사람의 풀이
def sum_ppg1(playerOne, playerTwo):
    return playerOne.get('ppg', 0) + playerTwo.get('ppg', 0)

iverson = {'team': '76ers', 'ppg': 11.2}
jordan = {'team': 'bulls', 'ppg': 20.2}
print(31.4, sum_ppg(iverson, jordan))