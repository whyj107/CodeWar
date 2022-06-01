# Define a card suit
# https://www.codewars.com/kata/5a360620f28b82a711000047/train/python

# 나의 풀이
def define_suit(card):
    c = {'C': 'club', 'D': 'diamond', 'H': 'heart', 'S': 'spade'}
    return c[card[-1]] + 's'

# 다른 사람의 풀이
def define_suit1(card):
    return {'C':'clubs','D':'diamonds','H':'hearts','S':'spades'}[card[-1]]

print(define_suit('3C'), 'clubs')
print(define_suit('QS'), 'spades')
print(define_suit('9D'), 'diamonds')
print(define_suit('JH'), 'hearts')