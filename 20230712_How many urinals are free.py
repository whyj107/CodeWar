# How many urinals are free?
# https://www.codewars.com/kata/5e2733f0e7432a000fb5ecc4/train/python

# 나의 풀이
def get_free_urinals(urinals):
    if '11' in urinals: return -1
    return urinals.replace('10', '1').replace('01', '1').replace('00','0').count('0')

# 다른 사람의 풀이
def get_free_urinals1(urinals):
    return -1 if '11' in urinals else sum(((len(l)-1)//2 for l in f'0{urinals}0'.split('1')))

def get_free_urinals2(urinals):
    if urinals.count('11'): return -1
    return urinals.replace('10', '1').replace('01', '1').replace('00','0').count('0')