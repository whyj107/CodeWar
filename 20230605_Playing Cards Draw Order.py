# Playing Cards Draw Order – Part 1
# https://www.codewars.com/kata/630647be37f67000363dff04/train/python

# 나의 풀이
def draw(deck):
    drawn_cards = []
    tmp = True
    while deck:
        _ = deck.pop(0)
        if tmp:
            drawn_cards.append(_)
        else:
            deck.append(_)
        tmp = False if tmp else True
    return drawn_cards

# 다른 사람의 풀이
def draw1(deck):
    order = []
    while deck:
        order.append(deck.pop(0))
        if deck:
            deck.append(deck.pop(0))
    return order

sample_test_cases = [
    (['AH','2H','3H','4H'],                      ['AH','3H','2H','4H']),
    (['KC','KH','QC','KS','KD','QH','QD','QS'],  ['KC','QC','KD','QD','KH','QH','KS','QS']),
    (['5D','3C','XR'],                           ['5D','XR','3C']),
    (['8H','8C','7H','XB','9S'],                 ['8H','7H','9S','XB','8C']),
    ([],                                         []),
]

for deck, expected in sample_test_cases:
    cards = ','.join(map(repr, deck))
    print(draw(deck), expected, f'draw([{cards}])')