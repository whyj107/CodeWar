# Rock Paper Scissors Lizard Spock
# https://www.codewars.com/kata/57d29ccda56edb4187000052/train/python

# 나의 풀이
def rpsls(pl1, pl2):
    draw = 'Draw!'
    pl1won = 'Player 1 Won!'
    pl2won = 'Player 2 Won!'
    rock = {'rock': draw, 'scissors': pl1won, 'paper': pl2won, 'lizard': pl1won, 'spock': pl2won}
    scissors = {'rock': pl2won, 'scissors': draw, 'paper': pl1won, 'lizard': pl1won, 'spock': pl2won}
    paper = {'rock': pl1won, 'scissors': pl2won, 'paper': draw, 'lizard': pl2won, 'spock': pl1won}
    lizard = {'rock': pl2won, 'scissors': pl2won, 'paper': pl1won, 'lizard': draw, 'spock': pl1won}
    spock = {'rock': pl1won, 'scissors': pl1won, 'paper': pl2won,
             'lizard': pl2won, 'spock': draw}
    result = {'rock': rock, 'scissors': scissors, 'paper': paper,
              'lizard': lizard, 'spock': spock}
    return result[pl1][pl2]

# 다른 사람의 풀이
ORDER = "rock lizard spock scissors paper spock rock scissors lizard paper rock"
def rpsls1(p1, p2):
    return ("Player 1 Won!" if f"{p1} {p2}" in ORDER else "Player 2 Won!" if f"{p2} {p1}" in ORDER else "Draw!")

win = {
    "scissors": {"paper", "lizard"},
    "paper": {"rock", "spock"},
    "rock": {"lizard", "scissors"},
    "lizard": {"spock", "paper"},
    "spock": {"scissors", "rock"}
}

def rpsls2(pl1, pl2):
    return pl2 in win[pl1] and "Player 1 Won!" or pl1 in win[pl2] and "Player 2 Won!" or "Draw!"



print(rpsls('rock', 'lizard'), 'Player 1 Won!')
print(rpsls('paper', 'rock'), 'Player 1 Won!')
print(rpsls('scissors', 'lizard'), 'Player 1 Won!')
print(rpsls('lizard', 'paper'), 'Player 1 Won!')
print(rpsls('spock', 'rock'), 'Player 1 Won!')
print(rpsls('lizard', 'scissors'), 'Player 2 Won!')
print(rpsls('spock', 'lizard'), 'Player 2 Won!')
print(rpsls('paper', 'lizard'), 'Player 2 Won!')
print(rpsls('scissors', 'spock'), 'Player 2 Won!')
print(rpsls('rock', 'spock'), 'Player 2 Won!')
print(rpsls('rock', 'rock'), 'Draw!')
print(rpsls('spock', 'spock'), 'Draw!')