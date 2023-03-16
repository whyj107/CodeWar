# [Mystery #1] - Cute Pattern
# https://www.codewars.com/kata/64087fd72daf09000f60dc26/train/python

# 나의 풀이
def cute_pattern(tiles):
    tiles = tiles.split()
    for i in range(3):
        for j in range(3):
            if tiles[i][j] == tiles[i][j+1] == tiles[i+1][j] == tiles[i+1][j+1]:
                return False
    return True

# 다른 사람의 풀이
import re

def cute_pattern1(tiles):
    return not re.search(r"BB...BB|WW...WW", tiles, re.DOTALL)