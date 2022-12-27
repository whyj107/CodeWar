# The 12 Days of Christmas
# https://www.codewars.com/kata/57dd3a06eb0537b899000a64/train/python

# 나의 풀이
def song_sorter(lines):
    tmp = []
    for idx, line in enumerate(lines):
        t = line.split(' ')[0]
        if t.isnumeric():
            tmp.append((int(t), line))
        elif t == 'On':
            tmp.append((13, line))
        elif t == 'a':
            tmp.append((1, line))
    return [j for i, j in sorted(tmp, reverse=True)]

# 다른 사람의 풀이
def song_sorter1(lines):
    return sorted(lines, key=lambda x: ['On', '12', '11', '10', '9', '8', '7', '6', '5', '4', '3', '2', 'and', 'a'].index(x.split()[0]))

real_lines = [
    "On the 12th day of Christmas my true love gave to me",
    "12 drummers drumming,",
    "11 pipers piping,",
    "10 lords a leaping,",
    "9 ladies dancing,",
    "8 maids a milking,",
    "7 swans a swimming,",
    "6 geese a laying,",
    "5 golden rings,",
    "4 calling birds,",
    "3 French hens,",
    "2 turtle doves and",
    "a partridge in a pear tree."
]

import random
shuffled_lines = real_lines.copy()
random.shuffle(shuffled_lines)
print(song_sorter(shuffled_lines), "Christmas is cancelled!")