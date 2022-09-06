# Mathemagics: the 21 Cards Trick
# https://www.codewars.com/kata/62b76a4f211432636c05d0a9/train/python

# 풀이
DECK = [1, 2, 3, 4, 5, 6, 7,
        8, 9, 10, 11, 12, 13, 14,
        15, 16, 17, 18, 19, 20, 21]

def guess_the_card(audience):
    deck = DECK[:]
    for i in range(3):
        decks = [deck[j::3] for j in range(3)]
        deck = decks.pop(audience.get_input(decks))
        deck = decks[0] + deck + decks[1]
    return deck[10]

# 다른 사람의 풀이
def guess_the_card1(audience):
    return audience.get_input([[n for n in DECK if n % 3 == p] for p in (0, 1, 2)]) \
     + 3 * audience.get_input([[n for n in DECK if (n//3) % 3 == p] for p in (0, 1, 2)]) \
     + 9 * audience.get_input([[n for n in DECK if (n//9) % 3 == p] for p in (0, 1, 2)])

class Audience:
    def __init__(self, n):
        self.n = n

    def get_input(self, array):
        for i, a in enumerate(array):
            if self.n in a:
                return i

card = 10
audience = Audience(card)
print(guess_the_card(audience), card)
