# FIRE and FURY
# https://www.codewars.com/kata/59922ce23bfe2c10d7000057/train/python

# 나의 풀이
from itertools import groupby
def fire_and_fury(tweet):
    if len(set(tweet) - set(['E', 'F', 'I', 'R', 'U', 'Y'])) > 0:
        return 'Fake tweet.'
    dic = {"FIRE": lambda x: f'You {"and you "*x}are fired!',
           "FURY": lambda x: f'I am {"really "*x}furious.'}
    tweet = tweet.replace('FURY', ' FURY ').replace('FIRE', ' FIRE ')
    tweet = [t for t in tweet.split(' ') if t in ['FIRE', 'FURY']]
    result = [dic[_](len(list(g))-1) for _, g in groupby(tweet)]
    return "Fake tweet." if len(result) == 0 else ' '.join(result)

print(fire_and_fury("FURYYYFIREYYFIRE"), "I am furious. You and you are fired!")
print(fire_and_fury("FIREYYFURYYFURYYFURRYFIRE"), "You are fired! I am really furious. You are fired!")
print(fire_and_fury("FYRYFIRUFIRUFURE"), "Fake tweet.")